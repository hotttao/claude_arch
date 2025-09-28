# CloudeWego 演示项目

## 1. 项目介绍

IDL 定义了四个服务:
1. trade: 量化交易微服务，包括
    - Account Service 获取账户信息，包括账户余额
    - Order Service 股票买卖接口
2. stock: 股票信息微服务，用于获取股票交易数据
3. strategy: 量化策略微服务，获取量化策略的筛选的股票
4. gateway: Hertz 网关微服务

服务之间会发生如下的调用链:
1. gateway 请求:
    - strategy
    - stock
    - trade
2. strategy 请求:
    - stock


## 2. 代码生成
### 2.1 生成 gRPC 代码

```bash
# 1. 生成 grpc 脚手架代码
kitex -module cloudewego idl/stock/trade.proto
kitex -module cloudewego idl/strategy/strategy.proto
kitex -module cloudewego idl/trade/account.proto
kitex -module cloudewego idl/trade/order.proto



# 2. 生成 kitex service 代码
mkdir stock
cd stock
kitex -module cloudewego  -service quant.stock -I ..\idl\ -use cloudewego/kitex_gen ..\idl\stock\trade.proto

mkdir strategy
cd strategy
kitex -module strategy  -service quant.strategy -I ..\idl\ ..\idl\strategy\strategy.proto
```