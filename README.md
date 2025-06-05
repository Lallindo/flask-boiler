# Boilerplate para aplicações Flask #

## Endpoints ##
Configure todos seus blueprints no arquivo "/configs.toml"

## Error Handlers ##
"error_handler" customizado deve ser feito em "/services/error_handler_loader.py"

## Páginas HTML ##
As páginas, seus scripts e seus css's devem ser descritos no arquivo *config.toml*

### Estrutura da configuração ###
```toml
[[scripts]]
    [scripts.nome_blueprint] # Dados de uma página
        html_title = html_file_path = "item.html" # Caminho para a página HTML
        js_file_path = ["item.js"] # Lista de arquivos JS que devem ser linkados à página
        css_file_path = ["item.css"] # Lista de arquivos CSS que devem ser linkados à página
```