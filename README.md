# docker-ml
Docker を利用して Jupyter を構築する

## 題材

https://qiita.com/tanakadaichi_1989/items/f3138bc907d7feedd3d3

## 実行手順
### Docker コマンドを利用
Docker コンテナを作成、実行
```
cd docker-ml
docker compose up -d 
```

Docker コンテナの実行状況を確認する
```
docker ps
```

上記コマンドの実行結果
```
CONTAINER ID   IMAGE            COMMAND                   CREATED             STATUS             PORTS                                            NAMES
7b5b9230ebf7   docker-ml-wine   "/bin/sh -c 'jupyter…"   About an hour ago   Up About an hour   0.0.0.0:6006->6006/tcp, 0.0.0.0:8888->8888/tcp   docker-ml-wine-1
```

下記コマンドでコンテナの Python のバージョンを確認できる
```
docker exec -it 7b5 python --version
```

上記コマンドの実行結果
```
Python 3.10.9
```

### 4. Web ブラウザで　Jupyter を表示
Web ブラウザで下記アドレスにアクセスする
```
http://localhost:8888/
```

初回はトークンの入力を求められる
下記コマンドでトークンを確認する
```
docker compose logs
```

### Jupyter で Python を実行
```
run main.py
```
### 実行結果を確認
![スクリーンショット 2023-07-15 22.29.47.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/199441/e4b7fe63-89cd-18c5-ddae-97ad88d87536.png)

散布図も表示可能
![スクリーンショット 2023-07-15 22.30.31.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/199441/abb48535-f797-991c-e70e-cb1f3134ee95.png)

### 5. Docker コンテナの停止・削除
Docker コンテナの一覧を表示する
```
docker ps
```

上記コマンドの実行結果
```
CONTAINER ID   IMAGE            COMMAND                   CREATED             STATUS             PORTS                                            NAMES
7b5b9230ebf7   docker-ml-wine   "/bin/sh -c 'jupyter…"   About an hour ago   Up About an hour   0.0.0.0:6006->6006/tcp, 0.0.0.0:8888->8888/tcp   docker-ml-wine-1
```

Docker コンテナを停止する
```
docker stop 7b5
```

Docker コンテナを削除する
```
docker rm 7b5
```

### 6. Docker イメージの削除
Docker イメージの一覧を表示する
```
docker images
```

上記コマンド実行結果
```
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
docker-ml-wine       latest    3c9361d00629   15 hours ago   4.28GB
```
