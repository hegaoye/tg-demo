# coding=utf-8
import random
import string

a = string.ascii_letters + string.digits
key = []


def get_password(length=16):
    """
    生成隨機的密碼
    :return:
    """
    key = random.sample(a, length)
    keys = "".join(key)
    return keys


def get_method():
    """
     serger :
        rc4-md5,
        aes-128-gcm, aes-192-gcm, aes-256-gcm,
        aes-128-cfb, aes-192-cfb, aes-256-cfb,
        aes-128-ctr, aes-192-ctr, aes-256-ctr,
        camellia-128-cfb, camellia-192-cfb,
        camellia-256-cfb, bf-cfb,
        chacha20-ietf-poly1305,
        xchacha20-ietf-poly1305,
        salsa20, chacha20 and chacha20-ietf
      

      client:
        "bf-cfb",
        "seed-cfb",
        "aes-128-cfb",
        "aes-192-cfb",
        "aes-256-cfb",
        "aes-128-ofb",
        "aes-192-ofb",
        "aes-256-ofb",
        "camellia-128-cfb",
        "camellia-192-cfb",
        "camellia-256-cfb",
        "chacha20",
        "chacha20-ietf",
        "rc4-md5"
    :return:
    """
    method_list = [
        "aes-128-cfb",
        "aes-192-cfb",
        "aes-256-cfb",
        "camellia-128-cfb",
        "camellia-192-cfb",
        "camellia-256-cfb",
        "chacha20",
        "chacha20-ietf",
        "rc4-md5"
    ]
    index = random.randint(0, method_list.__len__() - 1)
    return method_list[index]



# docker run  --name 119.8.127.119-10000 -d --restart=always -p 10000:8388 -p 10000:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m aes-256-cfb
# docker run  --name 119.8.127.119-10002 -d --restart=always -p 10002:8388 -p 10002:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m aes-128-cfb
# docker run  --name 119.8.127.119-10003 -d --restart=always -p 10003:8388 -p 10003:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m aes-192-cfb
# docker run  --name 119.8.127.119-10007 -d --restart=always -p 10007:8388 -p 10007:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m camellia-128-cfb
# docker run  --name 119.8.127.119-10008 -d --restart=always -p 10008:8388 -p 10008:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m camellia-192-cfb
# docker run  --name 119.8.127.119-10009 -d --restart=always -p 10009:8388 -p 10009:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m camellia-256-cfb
# docker run  --name 119.8.127.119-10010 -d --restart=always -p 10010:8388 -p 10010:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m chacha20-ietf
# docker run  --name 119.8.127.119-10011 -d --restart=always -p 10011:8388 -p 10011:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m chacha20
# docker run  --name 119.8.127.119-10012 -d --restart=always -p 10012:8388 -p 10012:8388/udp shadowsocks/shadowsocks-libev ss-server -p 8388  -k PV0e1vOf8NZ2djTkp4gqU6ar7y5swEhxnBKImSYHFGQRLzJu -m rc4-md5
