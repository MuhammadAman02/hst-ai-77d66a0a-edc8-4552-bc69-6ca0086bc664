from typing import List, Optional
from pydantic import BaseModel

class Product(BaseModel):
    """Product model for e-commerce items."""
    id: int
    name: str
    price: float
    description: str
    image_url: str
    category: str
    rating: float
    discount_percent: Optional[float] = None
    
    @property
    def discounted_price(self) -> float:
        """Calculate the discounted price if a discount is available."""
        if self.discount_percent:
            return round(self.price * (1 - self.discount_percent / 100), 2)
        return self.price

# Sample product data
sample_products = [
    Product(
        id=1,
        name="Premium Wireless Headphones",
        price=199.99,
        description="Noise-cancelling headphones with premium sound quality",
        image_url="/static/images/headphones.jpg",
        category="Electronics",
        rating=4.8,
        discount_percent=15
    ),
    Product(
        id=2,
        name="Organic Cotton T-Shirt",
        price=29.99,
        description="Soft, comfortable t-shirt made from 100% organic cotton",
        image_url="/static/images/tshirt.jpg",
        category="Clothing",
        rating=4.5
    ),
    Product(
        id=3,
        name="Smart Fitness Watch",
        price=149.99,
        description="Track your fitness goals with this advanced smart watch",
        image_url="/static/images/watch.jpg",
        category="Electronics",
        rating=4.7,
        discount_percent=10
    ),
    Product(
        id=4,
        name="Leather Wallet",
        price=49.99,
        description="Handcrafted genuine leather wallet with RFID protection",
        image_url="/static/images/wallet.jpg",
        category="Accessories",
        rating=4.6
    ),
    Product(
        id=5,
        name="Stainless Steel Water Bottle",
        price=24.99,
        description="Eco-friendly, insulated water bottle that keeps drinks cold for 24 hours",
        image_url="/static/images/bottle.jpg",
        category="Home",
        rating=4.9
    ),
    Product(
        id=6,
        name="Wireless Charging Pad",
        price=39.99,
        description="Fast wireless charging for all Qi-enabled devices",
        image_url="/static/images/charger.jpg",
        category="Electronics",
        rating=4.4,
        discount_percent=20
    )
]

# Categories with icons
categories = [
    {"name": "Electronics", "icon": "devices"},
    {"name": "Clothing", "icon": "checkroom"},
    {"name": "Accessories", "icon": "watch"},
    {"name": "Home", "icon": "home"},
    {"name": "Beauty", "icon": "spa"},
    {"name": "Sports", "icon": "sports_soccer"}
]

# Testimonials
testimonials = [
    {
        "name": "Sarah Johnson",
        "image": "/static/images/testimonial1.jpg",
        "text": "I love the quality of products and the fast shipping. Will definitely shop here again!",
        "rating": 5
    },
    {
        "name": "Michael Chen",
        "image": "/static/images/testimonial2.jpg",
        "text": "Great customer service and easy returns. The product exceeded my expectations.",
        "rating": 5
    },
    {
        "name": "Emma Williams",
        "image": "/static/images/testimonial3.jpg",
        "text": "The website is so easy to navigate and I found exactly what I was looking for.",
        "rating": 4
    }
]