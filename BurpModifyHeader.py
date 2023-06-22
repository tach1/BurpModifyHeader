from burp import IBurpExtender
from burp import ISessionHandlingAction
from datetime import datetime
import re


class BurpExtender(IBurpExtender, ISessionHandlingAction):
    NAME = 'BurpModifyHeader'

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName(self.NAME)
        callbacks.registerSessionHandlingAction(self)
        print(self.NAME + " Load OK")
        return

    def getActionName(self):
        return self.NAME

    def performAction(self, current_request, macro_items):
        if not macro_items:
            return
        response_info = macro_items[-1].getResponse()
        if response_info is None:
            return
        response = self._helpers.analyzeResponse(response_info)
        # rows = list(response.getHeaders())
        rows = response_info[response.getBodyOffset():].tostring().splitlines()
        token = self._get_token(rows)
        if token is None:
            return
        request_info = self._helpers.analyzeRequest(current_request)
        request_body = current_request.getRequest()[
            request_info.getBodyOffset():]
        new_header = self._set_headers(request_info.getHeaders(), token)
        new_message = self._helpers.buildHttpMessage(new_header, request_body)
        current_request.setRequest(new_message)
        return

    def _get_token(self, rows):
        # REGEXP = r'^set-cookie: access_token=(?P<token>.*?);'
        REGEXP = r'"access_token":"(?P<token>.*?)"'
        r = re.compile(REGEXP, re.I)
        token = None
        tokens = [r.search(h).group('token') for h in rows if r.search(h)]
        if tokens:
            token = tokens[-1]
            print(datetime.now().isoformat(), token)
        return token

    def _set_headers(self, headers, token):
        HEADER = 'Authorization: Bearer '
        new_headers = [h for h in headers if not h.startswith(HEADER)]
        new_headers.append(HEADER + token)
        return new_headers
