from easy_choroplet_map import EasyChoroplethMap

if __name__ == '__main__':
    easy = EasyChoroplethMap()
 
    # Use random data
    # --------------------------------   
    easy.random_data()    
    easy.title      = 'Random Data'
    easy.subtitle   = '(2020)'
    easy.source     = 'https://www.random.org/'
    easy.create_map(file_path='result.png')

    # Use data from excel
    # --------------------------------
    easy.load_excel_data('./templates/template.xlsx')
       
    # easy.title = ''
    # easy.subtitle = ''
    # easy.source = ''

    # easy.create_map('')