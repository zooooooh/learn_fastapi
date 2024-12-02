from fastapi import FastAPI, APIRouter
from  .products.views import router as product_router


router = APIRouter()
router.include_router(router=product_router, prefix="/products")