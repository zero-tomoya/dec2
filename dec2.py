
import hashlib
import pyminizip
import os
import time,sys
import warnings
import getpass
import zipfilejpn
os.chdir(os.path.dirname(os.path.abspath(__file__)))
warnings.simplefilter('ignore')
chef=1
sys1=1


# zipファイルの圧縮

def pyzip(file):
    while True:
        #print('')
        plaintext=getpass.getpass(prompt=' パスワード (英数字)>> ')
        print('')
        plaintext2=getpass.getpass(prompt=' もう一度パスワードを入力 (英数字)>> ')
        if plaintext!=plaintext2:
            print('')
            print(' パスワードが一致しません')
            print('')
            print(' もう一度やり直してください')
            time.sleep(5)
            continue
        elif plaintext==plaintext2:
            break
    key=plaintext
    pass2=str(key)
    pass2=hashlib.sha256(pass2.encode()).hexdigest()
    print('')
    if file=="":
        filename=input(' 圧縮対象ファイル名 >> ')
    else:
        filename=file
    filename=filename.replace(' ', '')
    filename=filename.replace('\'', ' ')
    filename = filename.strip()
    name,ext = os.path.splitext(filename)
    if ext==".lnk":
        print(' 対応していないファイル形式です。')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    elif ext==".zip" or ext==".dec":
        print(' ZIP形式のファイルは圧縮することはできません。')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    sf=os.path.dirname(filename)
    sf=sf+"/"
    cdir=os.path.isdir(sf)
    if cdir!=True:
        print(' ディレクトリの存在が確認できませんでした')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    basename_without_ext=basename_without_ext+".dec"
    basefiles=os.path.basename(filename) 
    os.chdir(sf)
    d=os.path.isfile(filename)
    if d!=True:
        print('ファイルが存在しません...')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    try :
        # 圧縮関係(英数字以外のファイル名もちゃんと圧縮できる)
        pyminizip.compress(basefiles.encode('cp932'),"\\".encode('cp932'),basename_without_ext.encode('cp932'),pass2,int(9))
        print('')
        print(' 圧縮中　しばらくお待ちください。(ファイルサイズによっては時間がかかる場合があります)')
    except PermissionError:
        print(' エラー :アクセスが拒否されたため圧縮ファイルを作成できませんでした。')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    else:
        print(' 圧縮が完了しました。')
    time.sleep(5)

# ファイルの展開

# 英数字以外のファイル名は文字化けする

def openzip(file,chef):
    #print('')
    pass3=getpass.getpass(prompt=' パスワード (英数字)>> ')
    key=pass3
    pass2=str(key)
    pass2=hashlib.sha256(pass2.encode()).hexdigest()
    pass2=bytes(pass2,encoding = "utf-8")
    if file=="":
        filename=input(' 展開ファイル名 >> ')
    else:
        filename=file
    filename=filename.replace(' ', '')
    filename= filename.replace('\'', ' ')
    filename = filename.strip()
    sf=os.path.dirname(filename)
    sf=sf+'/'
    cdir=os.path.isdir(sf)
    if cdir!=True:
        print(' ディレクトリの存在が確認できませんでした')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    
    ext = os.path.splitext(filename)[1]
    name=os.path.splitext(os.path.basename(filename))[0]
    ext=str(ext)
    name=name+".dec"
    #name=name.encode('cp932')
    name=str(name)
    #cd=os.path.isfile(name)
    cd2=os.path.isfile(filename)
    if filename=="" or name=="":
        filename="ファイルパスが入力されていません"
    if cd2!=True:
        print('')
        print(' エラー：ファイルが見つかりません。')
        print('')
        print(' 対象ファイルパス: '+filename)
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    os.chdir(sf)
    
    if ext!=".dec":
        print(' 対応していないファイル形式です。')
        print('')
        print(ext)
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    try:
        print('')
        print('')
        chef=int(chef)
        if chef==1:
            k=input(' 続行しますか? ( Y or N )')
        else:
            k="y"
        if k=="Y" or k=="YES" or k=="y":
            print(' 展開中　しばらくお待ちください。(ファイルサイズによっては時間がかかる場合があります)')
            zipfilepointer=zipfilejpn.ZipFile(name,"r")# ここから展開関係
            zipfilepointer.extractall(sf,pwd=bytes(pass2))
            zipfilepointer.close() # 展開関係ここで終わり
        if k=="N" or k=="n" or k=="NO" or k=="no" or k=="":
            print('')
            print(' 展開をキャンセルしました。')
            print('')
            time.sleep(5)
            return
    except RuntimeError:
        print(' パスワードエラー: パスワードが間違っています。')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    except PermissionError:
        print(' エラー :アクセスが拒否されたため圧縮ファイルを展開できませんでした。')
        print('')
        input(' メニュー画面に戻るにはエンターキーを押してください')
        return
    else:
        print(' 展開が完了しました')
        print('')
        print(' 出力先フォルダ: '+sf)
        time.sleep(5)
# メニュー表示

# メニュー表示
c=-1
sys1=int(sys1)
if sys1==1:
    args = sys.argv
    count=len(args)
    if count==2:
        file1=args[-1]
        file=args[-1]
        ext = os.path.splitext(file1)[1]
        if ext==".zip":
            print('')
            print(' エラー：zipファイルの展開と圧縮には対応していません。')
            print('')
            input(' 続けるにはエンターキーを押してください')
        elif ext==".dec":
            openzip(file,chef)
            file=""
        elif ext!=".zip" or ext!="dec":
            pyzip(file)
            file=""
    else:
        file=""

zipfilepointer=0
while True:
    os.system('clear')
    print('')
    print('')
    print(' ******パスワードZIP圧縮ツール　Ver 4.0******')
    print('')
    print(' 0:ファイルのパスワードZIP圧縮')
    print('')
    print(' 1:パスワードZIPファイルの展開')
    print('')
    print(' 終了するには[N]を入力してください')
    print('')
    print(' ************')
    print('')
    c= input(' 操作ID (0 or 1) >> ')
    if c!="N" and c!="n":
        try:
            c=int(c)
        except ValueError:
            pass
    #os.system('cls')
    if c==0:
        file=""
        pyzip(file)
        continue
    if c==1:
        file=""
        openzip(file,chef)
        continue
    if c=="N" or c=="n":
        print('')
        print(' プログラムを終了しています。')
        time.sleep(5)
        sys.exit()
