# BurpModifyHeader
JWT認証のアクセストークンが期限切れのとき、自動的に新しいアクセストークンを取得して再送するBurp Extensionです。
カスタマイズすることが前提です。

## Features
- Burpのマクロ機能を使ってリクエストを送信し、ヘッダもしくはボディから正規表現でアクセストークンを抽出します。
- 抽出したアクセストークンをヘッダに設定して、元のリクエストを再送します。

## Usage
1. メニューの [Setting]->[Extentions]->[Python environment]に jythonの jarファイルを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/5eaf570a-7a99-4ea1-86c5-0c188a0aa1a5)

2. [Extension]->[Add]->[Extension details]に、この Burp Extensionを指定し、[Next]でロードします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/0263ec40-d677-402e-8637-4e153f6017b6)

3. アクセストークンを取得するリクエストを送信し、Burpでキャプチャします。
   
![](https://github.com/tach1/BurpModifyHeader/assets/65728850/d7968fe6-17c1-4b7b-88ea-d9932ee04720)

4. [Settings]->[Sessions]->[Macros]->[Add]と進み、上でキャプチャしたリクエストを登録しておきます。細かな設定は不要です。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/a1e8ec35-6b7a-48c3-bef5-1150e2e8051f)

4. [Settings]->[Sessions]->[Session handling rules]->[Add]->[Rule actions]->[Add]と進み、[Check session is valid]を選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/c494134e-0103-47b8-9f1d-24b830c2bda6)

5. ここでは、例として HTTPヘッダが 403を返したときアクセストークンが期限切れと見なします。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/8178f780-d766-4ff0-9e31-f0601c97bdf7)

6. [If session is invalid, perform the action below:]に、上で登録したマクロを選択します。また、[After running the macro, invoke a Burp extension action handler:]に、この Burp Extensionを選択します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/a43ec5c2-5dee-44f1-b12b-2bdb6dd856aa)

7. 最後にターゲットとなるスコープを指定します。

![](https://github.com/tach1/BurpModifyHeader/assets/65728850/9835217b-d6ea-41aa-b37d-a929db8b19d0)

8. アクセストークンを取得するための正規表現や、更新対象とするヘッダは、適宜 BurpModifyHeader.pyを編集してください。


## Build
```
git clone https://github.com/tach1/BurpModifyHeader.git
cd BurpModifyHeader

-> BurpModifyHeader.py
```

## Lisense
[MIT](https://github.com/tach1/BurpModifyHeader/blob/main/LICENSE)
