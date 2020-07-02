##
## Dont change this file,if you dont understand
##

## すべてローカル環境側の設定

ssh_config_host="vagrant"

loginuser="vagrant"

secret_key="ansible_ecdsa"

password_file="ansible_password.yml"

# you want to use ssh directory.
# ex) ./.ssh #-> inside of project
# ex) $HOME/.ssh #-> you using user .ssh
ssh_directory=./.ssh

secret_key_path=$ssh_directory/$secret_key

# sshでログイン用のプロジェクト配下に作成
mkdir -m 700 $ssh_directory

# vagrant(server)側の設定をクライアント側のPCに書く。
vagrant ssh-config  --host $ssh_config_host >> $ssh_directory/config

# scpは非推奨になったためsftpで実装
sftp -F $ssh_directory/config $ssh_config_host  <<END
lcd ./.ssh/
get /home/$loginuser/$secret_key
END

# scpは非推奨になったためsftpで実装
sftp -F ./.ssh/config $ssh_config_host  <<END
get /home/$loginuser/$password_file
END

# 秘密鍵をダウンロードしたので、安全のためサーバー側の秘密鍵を削除
ssh -F $ssh_directory/config $ssh_config_host rm /home/$loginuser/$secret_key

# パスワードファイルをダウンロードしたので、安全のためサーバー側のパスワードファイルを削除
ssh -F $ssh_directory/config $ssh_config_host rm /home/$loginuser/$password_file

# 秘密鍵を使うためにパーミッション変更
chmod 600 $ssh_directory/$secret_key

# User,IdentityFileをansibleの物に変更
vagrant ssh-config  --host ${ssh_config_host}_ansible | 
    sed "s/User $loginuser/User ansible/" |
    sed -E "s|IdentityFile .*$|IdentityFile $ssh_directory/$secret_key|" >> $ssh_directory/config

# ansibleが秘密鍵を使うためのユーザーを作成
ansible-vault encrypt $password_file

# セキュリティ上、rootユーザーの環境変数を引き継ぐ、もしくは指定される形で実行する。
# アプリケーションのユーザー名
read -p "input site username>" PUPPETEER_USERNAME
ssh -F $ssh_directory/config $ssh_config_host "echo export PUPPETEER_USERNAME=$PUPPETEER_USERNAME >> /home/$loginuser/.profile"

# アプリケーションのパスワード名
read -sp "input site password>" PUPPETEER_PASSWORD
ssh -F $ssh_directory/config $ssh_config_host "echo export PUPPETEER_PASSWORD=$PUPPETEER_PASSWORD >> /home/$loginuser/.profile"
