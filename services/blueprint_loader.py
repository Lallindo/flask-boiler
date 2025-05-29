import importlib
import toml
from flask import Blueprint

def _register_blueprints(app, arquivo_toml_config):
    """
    Lê um arquivo TOML, importa dinamicamente e registra os blueprints no app Flask.

    Args:
        app (Flask): A instância da aplicação Flask.
        arquivo_toml_config (str): O caminho para o arquivo TOML de configuração.
    """
    
    try:
        config = toml.load(arquivo_toml_config)
        print(f"Configuração carregada de '{arquivo_toml_config}': {config}.")
    except FileNotFoundError:
        print(f"Erro: Arquivo de configuração '{arquivo_toml_config}' não encontrado.")
        return
    except toml.TomlDecodeError:
        print(f"Erro: Falha ao decodificar o arquivo TOML '{arquivo_toml_config}'.")
        return
    
    if "blueprints" not in config:
        print(f"Aviso: Nenhuma seção 'blueprints' encontrada em '{arquivo_toml_config}'.")
        return
    
    for nome_bp_config, caminho_modulo_str in config['blueprints'].items():
        try:
            modulo = importlib.import_module(caminho_modulo_str)
            print(f"Módulo '{caminho_modulo_str} importado com sucesso'")
            
            blueprint_obj = None
            nome_variavel_bp = f"{nome_bp_config}_bp"
            if hasattr(modulo, nome_variavel_bp):
                blueprint_obj = getattr(modulo, nome_variavel_bp)
            else:
                for nome_attr in dir(modulo):
                    attr = getattr(modulo, nome_attr)
                    if isinstance(attr, Blueprint):
                        blueprint_obj = attr
                        print(f"Blueprint encontrado genericamente: '{nome_attr}' em  '{caminho_modulo_str}'")
            
            if blueprint_obj and isinstance(blueprint_obj, Blueprint):
                app.register_blueprint(blueprint_obj, url_prefix=f"/{nome_bp_config}")
                print(f"Blueprint '{getattr(blueprint_obj, "name", nome_bp_config)}' de '{caminho_modulo_str}' registrado com sucesso.")
            else:
                print(f"Aviso: Nenhum objeto Blueprint válido encontrado em '{caminho_modulo_str}' ou com o nome esperado '{nome_variavel_bp}'")
                
        except ImportError:
            print(f"Erro: Falha ao importar o módulo '{caminho_modulo_str}' para o blueprint '{nome_bp_config}'. Verifique o caminho.")
        except AttributeError:
            print(f"Erro: O módulo '{caminho_modulo_str}' não possui o atributo esperado para o blueprint '{nome_bp_config}'.")
        except Exception as e:
            print(f"Erro inesperado ao registrar blueprint '{nome_bp_config}' de '{caminho_modulo_str}': {e}")
