# BurpModifyHeader
JWT認証のアクセストークンが期限切れのとき、自動的に新しいアクセストークンを取得して再送するBurp Extensionです。
カスタマイズすることが前提です。

## Features
- Burpのマクロ機能を使ってリクエストを送信し、ヘッダもしくはボディから正規表現でアクセストークンを抽出します。
- 抽出したアクセストークンをヘッダに設定して、元のリクエストを再送します。

## Usage
1. メニューの [Setting]->[Extentions]->[Python environment]に jythonの jarファイルを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/491d70af-210f-4bb4-83d9-7a164c25d135)

2. [Extension]->[Add]->[Extension details]に、この Burp Extensionを指定し、[Next]でロードします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/2ded7f7f-501e-4ee8-b7cd-e4e04f4faf00)

3. アクセストークンを取得するリクエストを送信し、Burpでキャプチャします。
   
![](https://github.com/tach1/BurpModifyHeader/assets/65728850/dedf2f5c-ce64-4a70-ad9e-4752d986d49a)

4. [Settings]->[Sessions]->[Macros]->[Add]と進み、上でキャプチャしたリクエストを登録しておきます。細かな設定は不要です。

![スクリーンショット 2023-06-22 200423](https://github.com/tach1/BurpModifyHeader/assets/65728850/619c1017-fe8b-45e6-bef8-d1b94f7fed58)

5. [Settings]->[Sessions]->[Session handling rules]->[Add]->[Rule actions]->[Add]と進み、[Check session is valid]を選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/b6111384-b9c0-4d45-a767-cbfcaaa2e027)

6. ここでは、例として HTTPヘッダが 403を返したときアクセストークンが期限切れと見なします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/014d5ee7-a927-4a92-a087-bb1987a181f9)

7. [If session is invalid, perform the action below:]に、上で登録したマクロを選択します。また、[After running the macro, invoke a Burp extension action handler:]に、この Burp Extensionを選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/a83a8867-c79d-4246-bac6-731031ed2227)

8. 最後にターゲットとなるスコープを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/d45bcf00-5df3-4c15-b487-3707b9666b09)

9. アクセストークンを取得するための正規表現や、更新対象とするヘッダは、適宜 BurpModifyHeader.pyを編集してください。

## Build
```
git clone https://github.com/tach1/BurpModifyHeader.git
cd BurpModifyHeader

-> BurpModifyHeader.py
```

## Lisense
[MIT](https://github.com/tach1/BurpModifyHeader/blob/main/LICENSE)
