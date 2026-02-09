from django.shortcuts import render


def home(request):
    categories = [
        "Mobiles",
        "Fashion",
        "Electronics",
        "Home & Furniture",
        "Appliances",
        "Beauty & Toys",
        "Grocery",
    ]
    deals = [
        {
            "title": "Smartphone Fest",
            "price": "From ₹9,999",
            "badge": "Best Seller",
        },
        {
            "title": "Fashion Forward",
            "price": "Min 40% off",
            "badge": "Trending",
        },
        {
            "title": "Work From Home",
            "price": "Laptops under ₹39,999",
            "badge": "Limited Time",
        },
        {
            "title": "Kitchen Essentials",
            "price": "Up to 55% off",
            "badge": "Hot Deal",
        },
    ]
    services = [
        "Easy returns",
        "Free delivery on select items",
        "Secure payments",
        "24x7 customer support",
    ]
    return render(
        request,
        "home/index.html",
        {
            "categories": categories,
            "deals": deals,
            "services": services,
        },
    )
