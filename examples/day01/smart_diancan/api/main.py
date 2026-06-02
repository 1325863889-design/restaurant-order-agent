"""
智能点餐助手主程序 FastAPI 接口
1.定义FastAPI应用实例
2.提供三个主要接口：
2.1 POST /chat - 智能对话接口
2.2 POST /delivery - 配送查询接口
2.3 GET /menu/list - 菜品列表接口
"""


from  fastapi import  FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI(title="智能点餐助手的API接口",description="智能点餐应用主要暴露三个接口分别为智能对话接口、配送查询接口、菜品列表接口")



@app.get("/")
def  hello_world():
    """测试项目根路径访问是否可用"""
    return {"hello":"world"}

@app.get("/healthy")
def  healthy():
    """测试项目请求路径访问是否可用"""
    return {"message":"请求路径访问健康"}


# 定义数据模型
# 菜品列表展示
class MenuListResponse(BaseModel):
    """菜品列表响应"""
    success: bool   # 有数据：True 没数据False
    menu_items: List[dict] # 菜品列表
    count: int # 菜品数
    message: str # 响应消息提示




@app.get("/menu/list", response_model=MenuListResponse)
async def menu_list_endpoint():
    """菜品列表区域展示"""

    # 1.调用service
    from  smart_diancan.service.diancan_service import get_menu

    # 2.调用方法
    menu_items=get_menu()


    # 3.封装结果返回
    if  not  menu_items:
        return MenuListResponse(
            success=False,
            menu_items=[],
            count=0,
            message="暂无菜品列表可用"
        )

    return MenuListResponse(
        success=True,
        menu_items=menu_items,
        count=len(menu_items),
        message=f"成功查询到{len(menu_items)}道菜品信息"
    )





















