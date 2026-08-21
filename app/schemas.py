from pydantic import BaseModel

# 데이터를 생성할 때 필요한 내용들을 담은 변수에 대한 클라이언트가 보내야 하는 형태
class Prms2Create(BaseModel):
    customer_count: int
    product_count: tuple[int, int] # categories, products in each category
    order_count: int
    city_count: int
