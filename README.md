# BurpModifyHeader
JWT認証のアクセストークンが期限切れのとき、自動的に新しいアクセストークンを取得して再送するBurp Extensionです。
カスタマイズすることが前提です。

## Features
- Burpのマクロ機能を使ってリクエストを送信し、ヘッダもしくはボディから正規表現でアクセストークンを抽出します。
- 抽出したアクセストークンをヘッダに設定して、元のリクエストを再送します。

## Usage
1. メニューの [Setting]->[Extentions]->[Python environment]に jythonの jarファイルを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/fa0cd0ae-a970-41ff-a577-e0f1bad20b7b)

2. [Extension]->[Add]->[Extension details]に、この Burp Extensionを指定し、[Next]でロードします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/149b42b0-c4d2-41bc-aab0-6814fc758b5b)

3. アクセストークンを取得するリクエストを送信し、Burpでキャプチャします。
   
![](https://github.com/tach1/BurpModifyHeader/assets/65728850/9e13d81e-2049-435d-8825-654ebf8dddfd)

4. [Settings]->[Sessions]->[Macros]->[Add]と進み、上でキャプチャしたリクエストを登録しておきます。細かな設定は不要です。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/8cceb267-c6b2-4495-bcf9-0f395bf6c988)

5. [Settings]->[Sessions]->[Session handling rules]->[Add]->[Rule actions]->[Add]と進み、[Check session is valid]を選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/04f8d5f6-e30a-47dd-8a5a-0d944a102abf)

6. ここでは、例として HTTPヘッダが 403を返したときアクセストークンが期限切れと見なします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/845bd104-bc56-4ef9-bea2-c4287bec5199)

7. [If session is invalid, perform the action below:]に、上で登録したマクロを選択します。また、[After running the macro, invoke a Burp extension action handler:]に、この Burp Extensionを選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/239efb34-22e8-498b-b46f-a87510abccc2)

8. 最後にターゲットとなるスコープを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/9eb266fc-2b84-4564-ba2b-4f4eac4bb4fc)

9. アクセストークンを取得するための正規表現や、更新対象とするヘッダは、適宜 BurpModifyHeader.pyを編集してください。

## Build
```
git clone https://github.com/tach1/BurpModifyHeader.git
cd BurpModifyHeader

-> BurpModifyHeader.py
```

## Lisense
[MIT](https://github.com/tach1/BurpModifyHeader/blob/main/LICENSE)
