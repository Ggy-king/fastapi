from fastapi import FastAPI
# 从fastapi包 里面导入 FastAPI类  import fastapi 是将整个fastapi包导入进来

app = FastAPI(title = "我的跨端测试服务")  # 实例化 FastAPI类  创建一个FastAPI的实例对象

@app.get("/")  #装饰器 本质上是接受一个函数作为参数，并返回一个新的函数。它的作用是将被装饰的函数注册为一个路由处理函数
async def root():  # 定义一个异步函数 root()，它将作为根路径的请求处理函数
    return {"message": "服务运行成功","tip": "欢迎使用我的跨端测试服务" }  # 返回一个字典，FastAPI会将其自动转换为JSON格式的响应。 这里没有await本质上还是会作为同步函数处理。但是写async的话，fastapi会将其作为异步函数处理

@app.get("/hello/{name}") # 定义一个新的路由，路径为 /hello/{name}，其中 {name} 是一个路径参数
async def hello(name: str):  # 这里的str表示name参数的类型是字符串,fastapi会自动进行类型验证和转换
    return {"message": f"Hello, {name}!"}  # 返回一个字典，f的作用是格式化字符串，将name的值插入到字符串中

@app.post("/post-data") # 定义一个新的路由，路径为 /post，使用POST方法 post主要是用于接受客户端发送的数据
async def post_data(data: dict):  # dict是Python内置的数据类型，表示一个键值对的集合
    return {"status": "ok", "data": data}  # 返回一个字典，包含客户端发送的数据 
    