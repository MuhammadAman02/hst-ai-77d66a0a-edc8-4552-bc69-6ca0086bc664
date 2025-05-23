from nicegui import ui, app
import os
from app.models.product import sample_products, categories, testimonials

# Configure app
app.title = "ShopEase - Your One-Stop Shop"
app.favicon = "🛍️"

# Create a directory for static files if it doesn't exist
os.makedirs("app/static/css", exist_ok=True)
os.makedirs("app/static/images", exist_ok=True)

# Mount static files
app.add_static_files("/static", "app/static")

# Custom CSS
with open("app/static/css/styles.css", "w") as f:
    f.write("""
    /* Custom CSS for ShopEase */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        color: #333;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        padding: 2rem 1rem;
        text-align: center;
        border-radius: 0 0 20px 20px;
    }
    
    .section-title {
        text-align: center;
        margin: 2rem 0;
        color: #333;
        font-weight: bold;
    }
    
    .product-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 8px;
        overflow: hidden;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .category-card {
        text-align: center;
        padding: 1.5rem;
        border-radius: 8px;
        background-color: #f8f9fa;
        transition: all 0.3s ease;
    }
    
    .category-card:hover {
        background-color: #e9ecef;
        transform: translateY(-5px);
    }
    
    .testimonial-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .footer {
        background-color: #343a40;
        color: white;
        padding: 2rem 0;
        margin-top: 3rem;
    }
    
    .newsletter-section {
        background-color: #f1f3f5;
        padding: 2rem;
        border-radius: 8px;
        margin: 2rem 0;
    }
    
    .discount-badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: #dc3545;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-weight: bold;
    }
    
    .price-section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .original-price {
        text-decoration: line-through;
        color: #6c757d;
    }
    
    .discounted-price {
        font-weight: bold;
        color: #dc3545;
    }
    
    .rating {
        color: #ffc107;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .hero-section h1 {
            font-size: 1.8rem;
        }
        .hero-section p {
            font-size: 1rem;
        }
    }
    """)

# Create placeholder images
placeholder_images = {
    "headphones.jpg": "https://via.placeholder.com/300x300?text=Headphones",
    "tshirt.jpg": "https://via.placeholder.com/300x300?text=T-Shirt",
    "watch.jpg": "https://via.placeholder.com/300x300?text=Smart+Watch",
    "wallet.jpg": "https://via.placeholder.com/300x300?text=Wallet",
    "bottle.jpg": "https://via.placeholder.com/300x300?text=Water+Bottle",
    "charger.jpg": "https://via.placeholder.com/300x300?text=Charging+Pad",
    "testimonial1.jpg": "https://via.placeholder.com/100x100?text=Sarah",
    "testimonial2.jpg": "https://via.placeholder.com/100x100?text=Michael",
    "testimonial3.jpg": "https://via.placeholder.com/100x100?text=Emma",
    "logo.png": "https://via.placeholder.com/200x50?text=ShopEase"
}

# Main page
@ui.page('/')
def index():
    # Add viewport meta tag for responsiveness
    ui.add_head_html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    """)
    
    # Navigation bar
    with ui.header().classes('flex justify-between items-center p-4 bg-white shadow-sm'):
        ui.label('ShopEase').classes('text-xl font-bold text-primary')
        
        with ui.row().classes('gap-4'):
            ui.button('Home', icon='home').props('flat')
            ui.button('Products', icon='shopping_bag').props('flat')
            ui.button('Categories', icon='category').props('flat')
            ui.button('About', icon='info').props('flat')
            ui.button('Contact', icon='mail').props('flat')
            
        with ui.row().classes('gap-2'):
            ui.button(icon='search').props('flat round')
            ui.button(icon='shopping_cart').props('flat round')
            ui.button('Login', icon='login').props('outline')
    
    # Hero section
    with ui.container().classes('hero-section w-full py-16'):
        ui.label('Welcome to ShopEase').classes('text-4xl font-bold mb-4')
        ui.label('Your one-stop destination for quality products at amazing prices').classes('text-xl mb-6')
        with ui.row().classes('justify-center gap-4'):
            ui.button('Shop Now', icon='shopping_bag').classes('text-lg').props('rounded color=white')
            ui.button('Learn More', icon='info').classes('text-lg').props('rounded outline color=white')
    
    # Featured products section
    with ui.container().classes('max-w-screen-xl mx-auto px-4 py-8'):
        ui.label('Featured Products').classes('section-title text-2xl font-bold')
        
        with ui.grid(columns=3).classes('gap-6'):
            for product in sample_products[:6]:
                with ui.card().classes('product-card w-full'):
                    # Use placeholder URLs for images in development
                    image_filename = product.image_url.split('/')[-1]
                    image_url = placeholder_images.get(image_filename, product.image_url)
                    
                    ui.image(image_url).classes('w-full h-48 object-cover')
                    
                    if product.discount_percent:
                        ui.label(f"{int(product.discount_percent)}% OFF").classes('discount-badge')
                    
                    with ui.card_section():
                        ui.label(product.name).classes('text-lg font-bold')
                        ui.label(product.description).classes('text-sm text-gray-600 h-12 overflow-hidden')
                        
                        # Rating
                        with ui.row().classes('items-center mt-2'):
                            for _ in range(int(product.rating)):
                                ui.icon('star', color='warning').classes('text-sm')
                            if product.rating % 1 >= 0.5:
                                ui.icon('star_half', color='warning').classes('text-sm')
                            ui.label(f"{product.rating}").classes('text-sm ml-1')
                        
                        # Price section
                        with ui.row().classes('items-center mt-2'):
                            if product.discount_percent:
                                ui.label(f"${product.price}").classes('original-price')
                                ui.label(f"${product.discounted_price}").classes('discounted-price text-lg')
                            else:
                                ui.label(f"${product.price}").classes('font-bold text-lg')
                        
                        ui.button('Add to Cart', icon='add_shopping_cart').props('outline').classes('mt-2 w-full')
    
    # Categories section
    with ui.container().classes('max-w-screen-xl mx-auto px-4 py-8 bg-gray-50'):
        ui.label('Shop by Category').classes('section-title text-2xl font-bold')
        
        with ui.grid(columns=6).classes('gap-4'):
            for category in categories:
                with ui.card().classes('category-card'):
                    ui.icon(category['icon']).classes('text-4xl text-primary')
                    ui.label(category['name']).classes('mt-2 font-medium')
    
    # Testimonials section
    with ui.container().classes('max-w-screen-xl mx-auto px-4 py-8'):
        ui.label('What Our Customers Say').classes('section-title text-2xl font-bold')
        
        with ui.grid(columns=3).classes('gap-6'):
            for testimonial in testimonials:
                with ui.card().classes('testimonial-card'):
                    with ui.row().classes('items-center gap-4'):
                        # Use placeholder URLs for images in development
                        image_filename = testimonial['image'].split('/')[-1]
                        image_url = placeholder_images.get(image_filename, testimonial['image'])
                        
                        ui.image(image_url).classes('w-12 h-12 rounded-full object-cover')
                        ui.label(testimonial['name']).classes('font-bold')
                    
                    # Rating
                    with ui.row().classes('mt-2'):
                        for _ in range(testimonial['rating']):
                            ui.icon('star', color='warning').classes('text-sm')
                    
                    ui.label(testimonial['text']).classes('mt-2 text-gray-600 italic')
    
    # Newsletter section
    with ui.container().classes('max-w-screen-xl mx-auto px-4'):
        with ui.card().classes('newsletter-section'):
            ui.label('Subscribe to Our Newsletter').classes('text-xl font-bold mb-2')
            ui.label('Get the latest updates on new products and special offers').classes('mb-4')
            
            with ui.row().classes('items-end gap-2'):
                with ui.input('Your Email').props('outlined').classes('flex-grow'):
                    ui.icon('email')
                ui.button('Subscribe', icon='send').props('color=primary')
    
    # Footer
    with ui.footer().classes('footer w-full'):
        with ui.container().classes('max-w-screen-xl mx-auto px-4'):
            with ui.grid(columns=4).classes('gap-8'):
                # Company info
                with ui.column():
                    ui.label('ShopEase').classes('text-xl font-bold mb-4')
                    ui.label('Your one-stop destination for quality products at amazing prices').classes('text-sm')
                    
                    with ui.row().classes('mt-4 gap-2'):
                        ui.button(icon='facebook').props('flat round color=white')
                        ui.button(icon='twitter').props('flat round color=white')
                        ui.button(icon='instagram').props('flat round color=white')
                        ui.button(icon='youtube').props('flat round color=white')
                
                # Quick links
                with ui.column():
                    ui.label('Quick Links').classes('font-bold mb-4')
                    ui.link('Home', '/').classes('block mb-2 text-white hover:underline')
                    ui.link('Products', '/products').classes('block mb-2 text-white hover:underline')
                    ui.link('About Us', '/about').classes('block mb-2 text-white hover:underline')
                    ui.link('Contact', '/contact').classes('block mb-2 text-white hover:underline')
                
                # Customer service
                with ui.column():
                    ui.label('Customer Service').classes('font-bold mb-4')
                    ui.link('FAQ', '/faq').classes('block mb-2 text-white hover:underline')
                    ui.link('Shipping Policy', '/shipping').classes('block mb-2 text-white hover:underline')
                    ui.link('Return Policy', '/returns').classes('block mb-2 text-white hover:underline')
                    ui.link('Privacy Policy', '/privacy').classes('block mb-2 text-white hover:underline')
                
                # Contact info
                with ui.column():
                    ui.label('Contact Us').classes('font-bold mb-4')
                    
                    with ui.row().classes('items-center mb-2'):
                        ui.icon('location_on').classes('mr-2')
                        ui.label('123 Commerce St, City, Country')
                    
                    with ui.row().classes('items-center mb-2'):
                        ui.icon('phone').classes('mr-2')
                        ui.label('+1 (555) 123-4567')
                    
                    with ui.row().classes('items-center mb-2'):
                        ui.icon('email').classes('mr-2')
                        ui.label('support@shopease.com')
            
            ui.separator().classes('my-6')
            ui.label('© 2023 ShopEase. All rights reserved.').classes('text-center text-sm')

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="ShopEase - Your One-Stop Shop")