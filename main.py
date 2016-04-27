from Helper import get_books_list, get_purchase_variants

BEST_VARIANTS_COUNT = 5

books_list = get_books_list()
print("books_list:%s" % books_list)

variants = get_purchase_variants(books_list, BEST_VARIANTS_COUNT)
print("variants:%s" % variants)
