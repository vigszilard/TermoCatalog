"""Seed the database with dummy data for development."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')
django.setup()

from django.contrib.auth.models import User
from categories.models import Category, Gallery
from products.models import Product
from designs.models import Sandblast, Printing
from pages.models import AboutPage, ContactPage, FAQPage, DesignsPage, Partner

IMG = "https://th.bing.com/th/id/OIP.Wb2dLxE6iU5z_nf2BKdzrAHaHa?w=187&h=187&c=7&r=0&o=7&pid=1.7&rm=3"

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# Clear old data
Category.sorted_by_relevance.all().delete()
Product.objects.all().delete()
Sandblast.sorted_by_size.all().delete()
Printing.sorted_by_size.all().delete()
AboutPage.objects.all().delete()
ContactPage.objects.all().delete()
FAQPage.objects.all().delete()
DesignsPage.objects.all().delete()

# Categories
categories_data = [
    ("Sticla securizata", 1),
    ("Sticla termoizolanta", 2),
    ("Balustrade sticla", 3),
    ("Oglinzi decorative", 4),
    ("Cabine de dus", 5),
]
created_categories = []
for name, relevance in categories_data:
    cat = Category.sorted_by_relevance.create(
        name=name,
        display_img=IMG,
        description=f"<p>Descriere detaliata pentru categoria <strong>{name}</strong>. Oferim o gama larga de produse de inalta calitate.</p><ul><li>Calitate superioara</li><li>Preturi competitive</li><li>Garantie extinsa</li></ul>",
        relevance=relevance,
    )
    created_categories.append(cat)
    for i in range(1, 5):
        Gallery.objects.create(category=cat, photo=IMG)

# Products
products_data = [
    ("Sticla securizata", 4, 0),
    ("Sticla securizata", 6, 0),
    ("Sticla securizata", 8, 0),
    ("Termopan dublu", 0, 1),
    ("Termopan triplu", 0, 1),
    ("Balustrada simpla", 0, 2),
    ("Balustrada cu mana curenta", 0, 2),
    ("Oglinda rotunda", 0, 3),
    ("Oglinda dreptunghiulara", 0, 3),
    ("Cabina walk-in", 0, 4),
    ("Cabina cu usa batanta", 0, 4),
]
for name, number, cat_idx in products_data:
    Product.objects.create(
        name=name,
        number=number,
        category=created_categories[cat_idx],
        display_img=IMG,
        description=f"<p>Produs de calitate superioara: <strong>{name}</strong>.</p><p>Disponibil in mai multe dimensiuni si configuratii. Contactati-ne pentru o oferta personalizata.</p>",
    )

# Sandblast designs
for i in range(1, 16):
    Sandblast.sorted_by_size.create(
        name=f"Model sablare {i:02d}",
        image=IMG,
        wide=(i == 13),
        high=(i == 14),
    )

# Printing designs
for i in range(1, 16):
    Printing.sorted_by_size.create(
        name=f"Model printare {i:02d}",
        image=IMG,
        wide=(i == 13),
        high=(i == 14),
    )

# About page
AboutPage.objects.create(
    content="<h3>Despre Termototal</h3><p>Suntem o companie cu traditie in domeniul produselor din sticla si termoizolatie. De peste 20 de ani oferim solutii personalizate pentru clientii nostri.</p><p>Echipa noastra de specialisti va sta la dispozitie pentru orice cerinta.</p><ul><li>Experienta de peste 20 de ani</li><li>Echipamente moderne</li><li>Personal calificat</li></ul>"
)

# Contact page
ContactPage.objects.create(
    street_name="Crisului",
    street_number="10",
    city="Dej",
    region="Cluj",
    country="Romania",
    zip_code="405200",
    landline="0264-211-222",
    mobile="0745-123-456",
    primary_email="contact@termototal.ro",
    secondary_email="speciale@termototal.ro",
    schedule="Luni - Vineri: 08:00 - 17:00\nSambata: 09:00 - 13:00\nDuminica: Inchis",
)

# FAQ
faq_data = [
    ("Care este termenul de livrare?", "Termenul standard de livrare este de 5-10 zile lucratoare, in functie de complexitatea comenzii si disponibilitatea materialelor."),
    ("Oferiti servicii de montaj?", "Da, oferim servicii complete de montaj pentru toate produsele noastre. Echipa noastra de specialisti asigura o instalare profesionala."),
    ("Ce garantie oferiti?", "Toate produsele noastre beneficiaza de o garantie de minimum 2 ani. Pentru anumite categorii de produse, garantia poate fi extinsa."),
    ("Cum pot solicita o oferta de pret?", "Puteti solicita o oferta de pret direct de pe pagina produsului dorit, completand formularul de cerere oferta, sau ne puteti contacta telefonic."),
]
for question, answer in faq_data:
    FAQPage.objects.create(question=question, answer=answer)

# Designs page
DesignsPage.objects.create(
    sandblast=IMG,
    printing=IMG,
    content="<p>Oferim o gama variata de modele de <strong>sablare</strong> si <strong>printare</strong> pentru personalizarea produselor din sticla. Alegeti din catalogul nostru sau aduceti propriul design.</p>",
)

print("Done! Database re-seeded.")
print("Admin: admin / admin")
