# GPG Configuration

[TOC]

## Git Path

[GitHub KnowTech_Learning](https://github.com/kevinkda/KnowTech_Learning/blob/main/Computer_Science/Certs_Key/GPG.md)



## Reference

- [Reference A](https://www.wevg.org/archives/gpg-sign-via-yubikey/)
- [Reference B](https://www.5axxw.com/wiki/content/vty5cc)
- [Reference C](https://blog.csdn.net/caiwenzhe/article/details/124559900)
- [Reference D](https://haoyu.love/blog523.html)
- [Reference E - YubiKey](https://www.wenjiangs.com/doc/tkg8bhlwg)
- [Reference F - YubiKey](https://haoyu.love/blog523.html)
- [Reference G - YubiKey](https://support.yubico.com/hc/en-us/articles/360013761339-Resetting-the-OpenPGP-Application-on-the-YubiKey)
- [Reference H](https://blog.csdn.net/nyist_zxp/article/details/107597626)
- [Reference I](https://www.dandelioncloud.cn/article/details/1497379405814140930)
- [Reference J](https://blog.csdn.net/willingtolove/article/details/122362705)



## GPG 官网

[gnupg.org](https://www.gnupg.org/)



<br/>

---

<br/>



## 生成 GPG 证书

### 创建主密钥

首先，输入 `gpg --expert --full-generate-key` 开始生成 GPG 证书，不要将主密钥设置为过期

```shell
$ gpg --expert --full-generate-key

Please select what kind of key you want:
(1) RSA and RSA (default)
(2) DSA and Elgamal
(3) DSA (sign only)
(4) RSA (sign only)
(7) DSA (set your own capabilities)
(8) RSA (set your own capabilities)
(9) ECC and ECC
(10) ECC (sign only)
(11) ECC (set your own capabilities)
(13) Existing key
Your selection? 1
```

输入 `1` 即选择 `(1) RSA and RSA (default)`，此处选择任意都可

> 需要注意的是，如果你的 Yubikey 型号为 NEO 那么请选择 `2048` 位，Yubikey 4 或 5 的话，选择 `4096` 位

```shell
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
0 = key does not expire
<n>  = key expires in n days
<n>w = key expires in n weeks
<n>m = key expires in n months
<n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y
```

输入您的个人信息，输入完成后如果没有问题输入 `o` 并敲击 `Enter` 键即可。

```shell
GnuPG needs to construct a user ID to identify your key.

Real name: Edison Jwa
Email address: example@uv.uy
Comment: 
You selected this USER-ID:
    "Edison Jwa <example@uv.uy>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
```

接下来会要求输入密码，请务必记住此密码。

```shell
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 1234567890ABCDEF marked as ultimately trusted
gpg: revocation certificate stored as '/home/edison/.gnupg/openpgp-revocs.d/W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP.rev'
public and secret key created and signed.

pub   rsa4096 2020-01-01 [SC] [expires: 2021-01-08]
      W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP
uid                      Edison Jwa <example@uv.uy>
sub   rsa4096 2020-01-01 [E] [expires: 2021-01-08]
```



### 生成子密钥

#### 方法一

至此，主证书已经创建完成，当然接下来我们继续添加子证书
输入 `gpg --expert --edit-key W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP` 开始对证书进行修改

```shell
edison@edison-pc ~> gpg --expert --edit-key W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP
gpg (GnuPG) 2.2.19; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: E   
[ultimate] (1). Edison Jwa <example@uv.uy>
```

输入 `addkey` 开始添加子证书

```shell
gpg> addkey 
Please select what kind of key you want:
   (3) DSA (sign only)
   (4) RSA (sign only)
   (5) Elgamal (encrypt only)
   (6) RSA (encrypt only)
   (7) DSA (set your own capabilities)
   (8) RSA (set your own capabilities)
  (10) ECC (sign only)
  (11) ECC (set your own capabilities)
  (12) ECC (encrypt only)
  (13) Existing key
  (14) Existing key from card
Your selection? 4
```

这里选择 `4`, 即 `RSA (sign only)`

```shell
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 1y
Key expires at Fri 08 Jan 2021 10:29:48 AM CST
Is this correct? (y/N) y
Really create? (y/N) y
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: S   
[ultimate] (1). Edison Jwa <example@uv.uy>
```

继续创建证书

```shell
gpg> addkey
Please select what kind of key you want:
   (3) DSA (sign only)
   (4) RSA (sign only)
   (5) Elgamal (encrypt only)
   (6) RSA (encrypt only)
   (7) DSA (set your own capabilities)
   (8) RSA (set your own capabilities)
  (10) ECC (sign only)
  (11) ECC (set your own capabilities)
  (12) ECC (encrypt only)
  (13) Existing key
  (14) Existing key from card
Your selection? 8
```

这里我们需要先去掉 `Sign` 和 `Encrypt` ，所依次输入 `S` `E`
接下来 输入 `A` 启用 `Authenticate`

```shell
Possible actions for a RSA key: Sign Encrypt Authenticate 
Current allowed actions: Sign Encrypt 

   (S) Toggle the sign capability
   (E) Toggle the encrypt capability
   (A) Toggle the authenticate capability
   (Q) Finished

Your selection? s

Possible actions for a RSA key: Sign Encrypt Authenticate 
Current allowed actions: Encrypt 

   (S) Toggle the sign capability
   (E) Toggle the encrypt capability
   (A) Toggle the authenticate capability
   (Q) Finished

Your selection? e

Possible actions for a RSA key: Sign Encrypt Authenticate 
Current allowed actions: 

   (S) Toggle the sign capability
   (E) Toggle the encrypt capability
   (A) Toggle the authenticate capability
   (Q) Finished

Your selection? a

Possible actions for a RSA key: Sign Encrypt Authenticate 
Current allowed actions: Authenticate 

   (S) Toggle the sign capability
   (E) Toggle the encrypt capability
   (A) Toggle the authenticate capability
   (Q) Finished

Your selection? q
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 1y
Key expires at Fri 08 Jan 2021 10:30:23 AM CST
Is this correct? (y/N) y
Really create? (y/N) y
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: S   
ssb  rsa4096/7EC20E50EE5ECDD5
     created: 2020-01-01  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>

gpg> save
```



#### 方法二

```shell
gpg --quick-add-key <fingerprint> rsa3072 encr 2y 
gpg --quick-add-key <fingerprint> rsa3072 auth 2y
gpg --quick-add-key <fingerprint> rsa3072 sign 2y
```

`<fingerprint>`需要填写的是主密钥的指纹，这个可以通过列出密钥来查看。
后面依次指定子密钥的加密算法、用途、有效时长。



### 查看生成的 GPG 证书

```shell
$ gpg --list-keys
/home/edison/.gnupg/pubring.kbx
-------------------------------
pub   rsa4096 2020-01-01 [SC] [expires: 2021-01-08]
      W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP
uid           [ultimate] Edison Jwa <example@uv.uy>
sub   rsa4096 2020-01-01 [E] [expires: 2021-01-08]
sub   rsa4096 2020-01-01 [S] [expires: 2021-01-08]
sub   rsa4096 2020-01-01 [A] [expires: 2021-01-08]

$ gpg --fingerprint --keyid-format long -K
/c/Users/Kevin/.gnupg/pubring.kbx
---------------------------------
sec   dsa3072/022117DA20445FA7 2022-06-06 [SC]
      Key fingerprint = 6AD1 D8AF EB92 668C CE9E  3558 0221 17DA 2044 5FA7
uid                 [ultimate] Kevin Tang <kevin_kda@yahoo.com.au>
ssb   elg3072/FC01E7D7A0887DB6 2022-06-06 [E]
ssb>  rsa4096/A6636E8ACFDE69F7 2022-06-06 [S] [expires: 2027-06-05]
ssb>  rsa4096/E3CC27DD82C72825 2022-06-06 [A] [expires: 2027-06-05]
ssb   nistp521/33B00D0F04A46C0D 2022-06-06 [S] [expires: 2027-06-05]
ssb   nistp521/3B511124247F7819 2022-06-06 [A] [expires: 2027-06-05]
ssb   nistp521/0DF307E13A4CF6FB 2022-06-06 [E] [expires: 2027-06-05]
ssb>  rsa4096/6E3CE54AE79A0E16 2022-06-06 [E] [expires: 2027-06-05]
```

#### 将电子邮件与 GPG 密钥关联

1. 使用 `gpg --list-secret-keys --keyid-format=long` 命令列出您拥有其公钥和私钥的长形式 GPG 密钥。 签名提交或标记需要私钥。

   ```shell
   $ gpg --list-secret-keys --keyid-format=long
   ```

   **注：**Linux上的一些 GPG 安装可能需要使用 `gpg2 --list-keyid-form LONG` 查看您现有密钥的列表。 在这种情况下，您还需要运行 `git config --global gpg.program gpg2` 来配置 Git 使用 `git gpg2`。

2. 从 GPG 密钥列表中复制您想要使用的 GPG 密钥 ID 的长形式。 在此例中，GPG 密钥 ID 是 `3AA5C34371567BD2`：

   ```shell
   $ gpg --list-secret-keys --keyid-format=long
   /Users/hubot/.gnupg/secring.gpg
   ------------------------------------
   sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
   uid                          Hubot 
   ssb   4096R/42B317FD4BA89E7A 2016-03-10
   ```

3. 输入 `gpg --edit-key GPG key ID`，替换要使用的 GPG 密钥 ID。 在以下示例中，GPG 密钥 ID 是 `3AA5C34371567BD2`：

   ```shell
   $ gpg --edit-key 3AA5C34371567BD2
   ```

4. 输入 `gpg> adduid` 以添加用户 ID 详细信息。

   ```shell
   $ gpg> adduid
   ```

5. 按照提示提供您的真实姓名、电子邮件地址和任何注释。 您可以选择 `N`、`C` 或 `E` 来修改各个条目。 要保持您的电子邮件地址私密，请使用 GitHub 提供的 `no-reply` 电子邮件地址。 更多信息请参阅“[设置提交电子邮件地址](https://docs.github.com/cn/articles/setting-your-commit-email-address)”。

   ```shell
   Real Name: Octocat
     Email address: octocat@github.com
     Comment: GitHub key
     Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit?
   ```

6. 输入 `O` 以确认选择。

7. 输入密钥的密码。

8. 输入 `gpg> save` 以保存更改

   ```shell
   $ gpg> save
   ```

9. 输入 `gpg --armor --export GPG key ID`，替换要使用的 GPG 密钥 ID。 在以下示例中，GPG 密钥 ID 是 `3AA5C34371567BD2`：

   ```shell
   $ gpg --armor --export 3AA5C34371567BD2
   # Prints the GPG key, in ASCII armor format
   ```





### 修改主密钥有效期

这里我们修改主密钥有效期为永久，这样每年只需要更新子密钥即可以了。

如在前序步骤中已将主密钥设置永久有效期，请忽略此步骤。

```shell
$ gpg --expert --edit-key W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP
gpg (GnuPG) 2.2.19; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: S   
ssb  rsa4096/7EC20E50EE5ECDD5
     created: 2020-01-01  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>

gpg> expire
Changing expiration time for the primary key.
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: never       usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: S   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-01  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>

gpg> save
```

此时可以发现有效期已经修改成功，以后只需要每年更新子密钥即可。



### 备份 GPG 密钥

上述所有步骤都是在本机上进行的，也可以直接使用OpenPGP Card规范中，在硬件中生成密钥的功能。
我们需要导出公钥以及各密钥的私钥，以便进行其他工作。

> 请务必执行备份的操作，首先导入至 Yubikey 的密钥是无法提取出来的，其次也可以不会像我一样丢失之前的 GPG 密钥

```shell
$ gpg --fingerprint --keyid-format long -K
/c/Users/Kevin/.gnupg/pubring.kbx
---------------------------------
sec   dsa3072/022117DA20445FA7 2022-06-06 [SC]
      Key fingerprint = 6AD1 D8AF EB92 668C CE9E  3558 0221 17DA 2044 5FA7
uid                 [ultimate] Kevin Tang <kevin_kda@yahoo.com.au>
ssb   elg3072/FC01E7D7A0887DB6 2022-06-06 [E]
ssb>  rsa4096/A6636E8ACFDE69F7 2022-06-06 [S] [expires: 2027-06-05]
ssb>  rsa4096/E3CC27DD82C72825 2022-06-06 [A] [expires: 2027-06-05]
ssb   nistp521/33B00D0F04A46C0D 2022-06-06 [S] [expires: 2027-06-05]
ssb   nistp521/3B511124247F7819 2022-06-06 [A] [expires: 2027-06-05]
ssb   nistp521/0DF307E13A4CF6FB 2022-06-06 [E] [expires: 2027-06-05]
ssb>  rsa4096/6E3CE54AE79A0E16 2022-06-06 [E] [expires: 2027-06-05]

# Public Key
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_public_key.asc --export 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_public_key.pub --export 6AD1D8AFEB92668CCE9E3558022117DA20445FA7

# Main Private Key
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_private_key.asc --export-secret-key 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
# DSA
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_022117DA20445FA7_dsa_sec_key.asc --export-secret-key 022117DA20445FA7!
# Elgamal
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_FC01E7D7A0887DB6_elgamal_sec_key.asc --export-secret-key FC01E7D7A0887DB6!

# Sub Key
# RSA
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_A6636E8ACFDE69F7_rsa_sub_sign_key.asc --export-secret-key A6636E8ACFDE69F7!
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_E3CC27DD82C72825_rsa_sub_auth_key.asc --export-secret-key E3CC27DD82C72825!
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_6E3CE54AE79A0E16_rsa_sub_encr_key.asc --export-secret-key 6E3CE54AE79A0E16!
# ECC
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_33B00D0F04A46C0D_rsa_sub_sign_key.asc --export-secret-key 33B00D0F04A46C0D!
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_3B511124247F7819_rsa_sub_auth_key.asc --export-secret-key 3B511124247F7819!
$ gpg -ao 6AD1D8AFEB92668CCE9E3558022117DA20445FA7_0DF307E13A4CF6FB_rsa_sub_encr_key.asc --export-secret-key 0DF307E13A4CF6FB!
```



### 上传 GPG 证书公钥

```shell
gpg --keyserver hkp://pgp.mit.edu --send-keys 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
gpg --keyserver keyring.debian.org --send-keys 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
gpg --keyserver keyserver.ubuntu.com --send-keys 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
gpg --keyserver keys.openpgp.org --send-keys 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
```



### 删除密钥

#### 删除公钥

```shell
gpg --delete-keys 6C8A15CECD3DCC2741A7C590AB38BACE635A064C
```

#### 删除私钥

```shell
gpg --delete-secret-keys 6C8A15CECD3DCC2741A7C590AB38BACE635A064C
```




<br/>

---



## 导入OpenPGP Card

```shell
# 查看智能卡设备状态
$ gpg --card-status
# 写入GPG
$ gpg --edit-key <fingerprint> # 主密钥
# 选中第一个子密钥
key <fingerprint>
# 写入到智能卡
keytocard

## 依次进行，注意选择各个插槽以及密钥用途的对应。

# 保存修改并退出
save

# 再次查看设备状态，可以看到相关槽位有密钥信息了。
$ gpg --card-status
```



<br/>

---

## 导入GPG密钥

`gpg --import public-file.key / private-file.key` : 导入公钥或私钥，其中，导入私钥需要输入保护私钥的密码；

```shell
$ gpg --import public-file.key
gpg: 密钥 E6730F4374866065：公钥"Search2016 (Search2016) <Search2016@163.com>"已导入
gpg: 合计被处理的数量：1
gpg:           已导入：1
$ gpg -k
/root/.gnupg/pubring.kbx
------------------------
pub   rsa2048 2020-07-27 [SC]
      8AC0AB86C34ADC6ED110A5A9E6730F4374866065
uid           [ 未知 ] Search2016 (Search2016) <Search2016@163.com>
$ gpg --import private-file.key
gpg: 密钥 E6730F4374866065："Search2016 (Search2016) <Search2016@163.com>"未改变
gpg: 密钥 E6730F4374866065：私钥已导入
gpg: 合计被处理的数量：1
gpg:           未改变：1
gpg:       读取的私钥：1

gpg:       导入的私钥：1
$ 
```

您可能还需要运行`gpg --expert --edit-key <fingerprint>`，然后键入`trust`以证明您的**是您信任的某人(您自己)。

```shell
$ gpg --expert --edit-key 6AD1D8AFEB92668CCE9E3558022117DA20445FA7
gpg> trust
```



### 在对私钥进行操作时，避免弹窗输入密码

GPG 在新的版本中，在对私钥进行操作的时候（签名、导入等）需要输入密钥的密码，但是有时候我们并不希望弹框输入密码，更希望是通过脚本等方式执行 GPG 的一些操作，方法如下：

#### 直接输入密码

```shell
gpg --import  --pinentry-mode loopback --batch --passphrase password  private-file.key
```

```shell
$ gpg --import --pinentry-mode loopback --batch --passphrase 123456 private-file.key
gpg: 密钥 E6730F4374866065：“Search2016 (Search2016) <Search2016@163.com>”未改变
gpg: 密钥 E6730F4374866065：私钥已导入
gpg: 合计被处理的数量：1
gpg:           未改变：1
gpg:       读取的私钥：1
gpg:       导入的私钥：1
$ 
```

#### 将密码输入到文件里

```shell
gpg --import --pinentry-mode loopback --batch --passphrase-file password-file  private-file.key
```

```shell
$ gpg --import --pinentry-mode loopback --batch --passphrase-file password-file private-file.key
gpg: 密钥 E6730F4374866065：“Search2016 (Search2016) <Search2016@163.com>”未改变
gpg: 密钥 E6730F4374866065：私钥已导入
gpg: 合计被处理的数量：1
gpg:           未改变：1
gpg:       读取的私钥：1
gpg:       导入的私钥：1
$
```


文件`password-file`第一行为设置的密码，这两种方式都不提倡使用，如果真要使用建议使用第二中。





<br/>

---



## 新增 GPG 密钥到 GitHub 帐户

[新增 GPG 密钥到 GitHub 帐户](https://docs.github.com/cn/authentication/managing-commit-signature-verification/adding-a-new-gpg-key-to-your-github-account)





<br/>

---



## 设置 OpenPGP 卡

### 修改 Yubikey 默认 PIN 码

首先，我们修改掉 Yubikey 的默认 PIN 码，（PIN 和 Admin PIN）

输入 `gpg --card-edit` 开始进行修改

```shell
$ gpg --card-edit

×××××
```

此处会输出 Yubikey 的信息

输入 `admin` 启用管理员指令

```shell
gpg/card> admin
Admin commands are allowed
```

输入 `passwd` 开始修改 PIN 码

Yubikey 的 默认 PIN 码为 `123456`
默认 Admin PIN 码为 `12345678`

```shell
gpg/card> passwd
gpg: OpenPGP card no. ××××× detected

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? 1
```

输入 `1` ，修改 PIN 码，此处会要求输入默认 PIN 码，和新 PIN 码两次

> PIN 码的长度要求不低于 6 位

```shell
PIN changed.

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? 3
```

接下来，输入 `3` 开始修改 Admin PIN 码

> Admin PIN 码的长度要求不低于8位

```shell
PIN changed.

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? q

gpg/card> q
```



### 导入到 Yubikey

输入 `gpg --expert --edit-key`

```shell
edison@edison-pc ~> gpg --expert --edit-key W4IJICKJLQPX8CMB9IYZMVPSMCCJIHOTGSM2QFGP
gpg (GnuPG) 2.2.19; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: never       usage: SC  
     trust: ultimate      validity: ultimate
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: S   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>

gpg> key 1
```

选中 `key 1`

```shell
sec  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: never       usage: SC  
     trust: ultimate      validity: ultimate
ssb* rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: S   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>
```

> 此处的 `*` 表示该证书已被选中

然后输入 `keytocard` 将 GPG 证书导入至 Yubikey 中

```shell
gpg> keytocard
Please select where to store the key:
   (2) Encryption key
Your selection? 2

sec  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: never       usage: SC  
     trust: ultimate      validity: ultimate
ssb* rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: E   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: S   
ssb  rsa4096/1234567890ABCDEF
     created: 2020-01-09  expires: 2021-01-08  usage: A   
[ultimate] (1). Edison Jwa <example@uv.uy>
gpg> key 1
```

再次输入 `key 1` 取消选中，接下来重复此动作，分别导入 `key 2` 和 `key 3`

### 检查 Yubikey 上存储的密钥

输入 `gpg --card-status` 即可查看 Yubikey 上存储的信息

后面进行签名的操作就都一样啦





<br/>

---

<br/>



## 设置 Git commit/tag 时使用 GPG 签名

### 单次使用GPG签名提交

#### commit

当本地分支中的提交更改时，请将 S 标志添加到 git commit 命令

```shell
$ git commit -S -m "your commit message"
# Creates a signed commit
$ git push
# Pushes your local commits to the remote repository
```

#### tag

要对标记签名，请将 `-s` 添加到您的 `git tag` 命令

```shell
$ git tag -s mytag
# Creates a signed tag
$ git tag -v mytag
# Verifies the signed tag
```

### 配置Git使用公钥检查提交签名

```shell
git config --global user.signingkey [GPG-KEY-ID]
```

### 一个仓库的提交使用 GPG 签名验证

```shell
git config commit.gpgsign true
```

### 所有仓库 Git 提交时使用公钥加密

```shell
git config --global commit.gpgsign true
```

### 设置 Git 自动签名

```shell
git config --global tag.forceSignAnnotated true
```

当前用户目录下创建配置文件`~/.gnupg/gpg-agent.conf`，并根据需要配置

[Reference](https://www.it1352.com/2098134.html)

```properties
# 告诉gpg-agent将密码短语存储1小时
default-cache-ttl 3600

# 告诉gpg-agent将密码短语存储24小时
default-cache-ttl 86400
```



<br/>



### 故障解决

#### Git commit 时 No such file or directory - Windows

[Reference](https://stackoverflow.com/questions/64650021/git-commit-error-cannot-spawn-gpg-exe-no-such-file-or-directory)

```shell
error: cannot spawn gpg: No such file or directory
error: gpg failed to sign the data
fatal: failed to write commit object
```

出现以上或类似故障时，采用以下方法：

```shell
$ which gpg
/usr/bin/gpg
$ git config --global gpg.program /usr/bin/gpg
```

