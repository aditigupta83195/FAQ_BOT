
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

FAQ_DATA = [

  
  { "q": "What is ShopNest?", 
    "a": "ShopNest is an online shopping marketplace offering electronics, fashion, home essentials, groceries, and more with fast delivery." },

  { "q": "Where does ShopNest operate?", 
    "a": "ShopNest delivers to all major cities and towns across the country." },

  { "q": "Do you have a mobile app?", 
    "a": "Yes, the ShopNest app is available on both Android and iOS devices." },

  
  { "q": "How do I create an account?", 
    "a": "Click the Sign Up button, enter your email or mobile number, create a password, and verify your details." },

  { "q": "How do I reset my password?", 
    'a': "Click 'Forgot Password' on the login page and follow the instructions sent to your email or phone." },

  { "q": "How do I change my address?", 
    "a": "Go to Account → Manage Addresses → Add or Edit your delivery address." },

  { "q": "Can I have multiple delivery addresses?", 
    "a": "Yes, you can save multiple addresses and choose one during checkout." },

  
  { "q": "How do I track my order?", 
    "a": "Go to My Orders → Select the item → Track Order to see real-time delivery updates." },

  { "q": "Why is my order delayed?", 
    "a": "Order delays may happen due to high demand, weather issues, or courier delays. Check tracking for updates." },

  { "q": "Can I change my delivery address after placing an order?", 
    "a": "Address changes are possible only before the item is shipped." },

  { "q": "My order shows delivered but I didn’t receive it", 
    "a": "Check with neighbors or security. If still not found, contact support for assistance." },

  
  { "q": "What payment methods do you accept?", 
    "a": "ShopNest accepts credit/debit cards, UPI, net banking, cash on delivery, and digital wallets." },

  { "q": "Is cash on delivery available?", 
    "a": "Yes, COD is available on most products unless restricted by the seller." },

  { "q": "Why was my payment declined?", 
    "a": "Payment failures may occur due to low balance, network issues, or bank restrictions." },

  { "q": "Are my payment details secure?", 
    "a": "Yes, we use encrypted & PCI-compliant systems for secure transactions." },

  
  { "q": "How long does delivery take?", 
    "a": "Most orders are delivered within 1–5 business days depending on your location." },

  { "q": "Do you offer same-day or next-day delivery?", 
    "a": "Yes, express delivery is available in select cities." },

  { "q": "Do you charge for delivery?", 
    "a": "Standard delivery is free on eligible orders. Shipping fees apply to low-value orders." },

  { "q": "Can I schedule my delivery?", 
    "a": "Yes, scheduled delivery is available for selected appliances and large items." },

  
  { "q": "What is your return policy?", 
    "a": "Most items can be returned within 7–10 days of delivery if unused and in original packaging." },

  { "q": "How do I return a product?", 
    "a": "Go to My Orders → Select item → Return or Replace → Choose reason → Submit." },

  { "q": "When will I get my refund?", 
    "a": "Refunds are usually processed within 3–7 business days after the returned item is picked up." },

  { "q": "Can I replace an item?", 
    "a": "Yes, replacements are available for damaged, defective, or incorrect items." },

  { "q": "What items are not eligible for return?", 
    "a": "Some items like innerwear, perishable goods, and digital products are non-returnable." },


  { "q": "How do I become a seller on ShopNest?", 
    "a": "You can register as a seller by visiting shopnest.com/sell and completing the signup form." },

  { "q": "What are the seller fees?", 
    "a": "Fees depend on product category and include commission, shipping fee, and GST." },

  { "q": "How do sellers get paid?", 
    "a": "Seller earnings are transferred weekly to their registered bank account." },

  
  { "q": "Are all products on ShopNest original?", 
    "a": "Yes, we guarantee authenticity for all products sold by verified sellers." },

  { "q": "Do products come with a warranty?", 
    "a": "Yes, many electronics and appliances include manufacturer warranty." },

  { "q": "Can I request a demo or installation?", 
    "a": "Yes, demo and installation services are available for appliances and TVs." },

  
  { "q": "What is ShopNest Plus?", 
    "a": "ShopNest Plus is a premium membership offering free delivery, deals, and exclusive rewards." },

  { "q": "How do I subscribe to ShopNest Plus?", 
    "a": "Go to Account → ShopNest Plus → Choose a monthly or yearly plan." },

  { "q": "Do Plus members get faster delivery?", 
    "a": "Yes, Plus members get free & priority delivery benefits." },

  
  { "q": "How do I contact customer support?", 
    "a": "You can contact support via chat, email, or the helpline number available in the Help Center." },

  { "q": "What are customer service hours?", 
    "a": "Customer support is available 24/7 through chat and email." },

  { "q": "How long does it take to resolve an issue?", 
    "a": "Most issues are resolved within 24–48 hours depending on complexity." },

  
  { "q": "Is my personal information secure?", 
    "a": "Yes, we use encryption and strict privacy practices to keep your data safe." },

  { "q": "Do you share customer data with sellers?", 
    "a": "We only share delivery-related details when necessary for fulfilling orders." },

  { "q": "How can I delete my account?", 
    "a": "Go to Account → Security Settings → Delete Account and follow the steps." },

  
  { "q": "How do I apply a coupon?", 
    "a": "Enter your coupon code on the checkout page before making payment." },

  { "q": "Why is my coupon not working?", 
    "a": "Some coupons have usage limits, apply only to specific categories, or may be expired." },

  
  { "q": "Do you deliver groceries?", 
    "a": "Yes, groceries and household essentials are available with fast delivery." },

  { "q": "Is fresh produce available?", 
    "a": "Yes, fresh fruits, vegetables, and dairy are available in select locations." }
]

for item in FAQ_DATA:
    item["embedding"] = model.encode(item["q"]).tolist()