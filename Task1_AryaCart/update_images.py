import os, sys, shutil, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novacart.settings')
django.setup()
from store.models import Product

# Artifact directory where generated images are
art_dir = r'C:\Users\amang\.gemini\antigravity-ide\brain\a981e57e-c02c-488e-a4e5-ccfae3b29700'
media_dir = r'c:\Users\amang\Desktop\aryacart\media\products'

# Full Mapping: product name -> generated image filename prefix
image_map = {
    'MacBook Pro M3': 'macbook_pro_',
    'Sony WH-1000XM5': 'sony_headphones_',
    'Samsung 65" OLED TV': 'samsung_oled_tv_',
    'Apple AirPods Pro 2': 'airpods_pro_',
    'iPhone 16 Pro Max': 'iphone_16_pro_',
    'Samsung Galaxy S25 Ultra': 'galaxy_s25_',
    'Google Pixel 9 Pro': 'pixel_9_pro_',
    'Wireless Bluetooth Headphones': 'bluetooth_headphones_',
    '4K Ultra HD Monitor': 'monitor_4k_',
    'Mechanical Gaming Keyboard': 'gaming_keyboard_',
    'Wireless Charging Pad': 'charging_pad_',
    'Flagship Pro Smartphone': 'flagship_phone_',
    'Budget Smart Phone': 'budget_phone_',
    'Phone Case Premium': 'phone_case_',
    'Classic Denim Jacket': 'denim_jacket_',
    'Premium Leather Bag': 'leather_bag_',
    'Designer Watch': 'designer_watch_',
    'Classic Aviator Sunglasses': 'aviator_sunglasses_',
    'Premium Leather Jacket': 'leather_jacket_',
    'Ergonomic Office Chair': 'office_chair_',
    'Smart LED Desk Lamp': 'desk_lamp_',
    'Premium Bedsheet Set': 'bedsheet_set_',
    'Python Programming Guide': 'python_book_',
    'The Art of War': 'art_of_war_book_',
    'Django Web Development': 'django_book_',
    'Professional Yoga Mat': 'yoga_mat_',
    'Fitness Tracker Band Pro': 'fitness_tracker_pro_',
    'Adjustable Dumbbell Set Pro': 'adjustable_dumbbells_pro_',
    'Fitness Tracker Band': 'fitness_tracker_',
    'Adjustable Dumbbells Set': 'adjustable_dumbbells_',
    'Yoga Mat Pro': 'yoga_mat_pro_',
    'Atomic Habits': 'atomic_habits_book_',
    'Django for Professionals': 'django_pro_book_',
    'Clean Code by Robert Martin': 'clean_code_book_',
    'Cozy Throw Blanket': 'cozy_blanket_',
    'Running Shoes Pro': 'running_shoes_pro_',
    'Cotton Crew T-Shirt': 'cotton_tshirt_',
    'Running Sneakers Pro': 'running_sneakers_',
    'Smart LED Desk Lamp Pro': 'desk_lamp_',
    'Ergonomic Office Chair Pro': 'office_chair_',
}

# Find and copy images
count = 0
for product_name, prefix in image_map.items():
    # Find the generated image file
    matching = [f for f in os.listdir(art_dir) if f.startswith(prefix) and f.endswith('.png')]
    if not matching:
        print(f"  SKIP: {product_name} - no image found with prefix {prefix}")
        continue
    
    # Use the latest one
    src = os.path.join(art_dir, matching[-1])
    
    # Target filename
    safe_name = product_name.lower().replace(' ', '-').replace(' ', '-').replace('"', '').replace("'", '')
    dest_name = f'new_{safe_name}.png'
    dest = os.path.join(media_dir, dest_name)
    
    shutil.copy2(src, dest)
    
    # Update database
    try:
        product = Product.objects.get(name=product_name)
        product.image = f'products/{dest_name}'
        product.save()
        count += 1
        print(f"  OK: {product_name} -> {dest_name}")
    except Product.DoesNotExist:
        print(f"  DB MISS: {product_name}")

print(f"\nUpdated {count} products with new unique images.")
