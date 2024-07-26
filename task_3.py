import timeit
import functions  
import markdown

def measure_time(sort_func, data, data2):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data, data2)
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time

def load_data(filename):
    try:
        with open(filename, "r",encoding='utf8') as f:
            return f.read()
    except FileNotFoundError:
        return -1 
    
def main():
        
    raws = [load_data("doc1.txt"), load_data("doc2.txt")]  
    pattern = ["даних","sfvd"]

    header = "{:<32}|{:<20}|{:<20}| ".format("Algoritm", "Time", "Value")
    print("-"*len(header))
    print(header)
    print("-"*len(header)) 
    
    for raw in raws:    
        for pat in pattern:
            if raws.index(raw) == 0:
                part = "Стаття 1"
            else:
                part = "Стаття 2"  
              
            # kmp_search                
            row = 0            
            row = "{:<32}".format(functions.kmp_search.__name__ + f": - {part}") 
            v,ex_time = measure_time(functions.kmp_search, raw, pat)
            row += "|{:<20.5f}".format(ex_time) + "|{:<20}|".format(v)         
            print(row)
            
            # rabin_karp_search
            row = 0 
            row = "{:<32}".format(functions.rabin_karp_search.__name__ + f": - {part}") 
            v,ex_time = measure_time(functions.rabin_karp_search, raw, pat)
            row += "|{:<20.5f}".format(ex_time) + "|{:<20}|".format(v)         
            print(row)
            
            # boyer_moore_search
            row = 0 
            row = "{:<32}".format(functions.boyer_moore_search.__name__ + f": - {part}") 
            v,ex_time = measure_time(functions.boyer_moore_search, raw, pat)
            row += "|{:<20.5f}".format(ex_time) + "|{:<20}|".format(v)         
            print(row)
                        
if __name__ == "__main__":
    main() 
    

input_text = """
# Висновки щодо швидкості роботи алгоритму

Для статті 1 найшвидшим при проходженні всього тексту якого не існує виявився алгоритм kmp_search 
але з невеликою різницею з kmp_search

Для статті 2 найшвидшим при проходженні всього тексту якого не існує виявився алгоритм boyer_moore_search
але з невеликою різницею з kmp_search

Також для пошуку відомих даних ці два алгоритма показали себе з такоюж різницею як і при пошуку не відомих данних

Висновок: Обидва алгоритма зазначенні вище підходять для швидкого пошуку, за структурою коду на мою думку 
kmp_search буде простіший і в деяких випадках швидше ніж boyer_moore_search
"""
 
# Преобразование текста в HTML
output_html = markdown.markdown(input_text)
 
print(output_html)