import toml
from dataclasses import dataclass
from typing import Union

STANDARD_CONFIG_FILE = "pyconfig.toml"

@dataclass
class HtmlData:
    blueprint_name: str
    page_name: str
    js_file_path: Union[list[str], None] = None
    css_file_path: Union[list[str], None] = None
    
    def set_page_data(self, **kwargs) -> None:
        for k, val in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, val)
                
    def __repr__(self) -> str:
        return f"\
            Blueprint: {self.blueprint_name}\n\
            Página: {self.page_name}\n\
            Arquivos JS: {self.js_file_path}\n\
            Arquivos CSS: {self.css_file_path}"
            
    def to_dict(self) -> dict:
        return {
            "bp_name": self.blueprint_name,
            "page_name": self.page_name.replace(".html", ""),
            "js_paths": self.js_file_path,
            "css_paths": self.css_file_path,
            }
        
    def get_js_css_for_html(
        self
    ) -> dict:
        config = toml.load("pyconfig.toml")["htmls"]
        try:
            config[self.blueprint_name]
        except KeyError:
            raise KeyError
        else:
            page_data: Union[HtmlData, None] = next((i for i in config[self.blueprint_name] if i["html_file_path"] == self.page_name), None)
            if page_data is None:
                raise ValueError
            self.set_page_data(**page_data) # type: ignore
            return self.to_dict()
    
