FROM python:3.11-slim

# 環境変数で .venv をプロジェクト直下に作らせる
ENV PIPENV_VENV_IN_PROJECT=1

# 必要なパッケージやツールをインストール（pipenv と依存関係のインストール）
RUN apt-get update && apt-get install -y sudo \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install pipenv

# vscode ユーザーの作成（UID=1000はVS Codeと一致させる）
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY Pipfile Pipfile.lock /app/

# 権限変更（pipenv installをvscodeユーザーで行うため）
RUN chown -R $USERNAME:$USERNAME /app

# vscodeユーザーに切り替え
USER $USERNAME

# pipenvを使って依存関係をインストール（ロックファイルを基にインストール）
RUN pipenv install --deploy --ignore-pipfile

# アプリケーションの全体をコピー（vscodeユーザーの権限で）
COPY --chown=vscode:vscode . /app/

# ポート明示（任意）
EXPOSE 8000

# コンテナ起動時に実行するコマンドを設定
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
