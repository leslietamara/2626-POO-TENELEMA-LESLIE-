from __future__ import annotations

import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    """Encapsula la lectura y escritura de productos en formato JSON."""

    def __init__(self, ruta_archivo: str | Path | None = None) -> None:
        if ruta_archivo is None:
            base = Path(__file__).resolve().parents[1]
            self.ruta_archivo = base / "datos" / "productos.json"
        else:
            self.ruta_archivo = Path(ruta_archivo)

    def cargar_productos(self) -> list[Producto]:
        try:
            with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as error:
            print(
                f"Advertencia: el archivo de productos tiene un formato JSON inválido. "
                f"Se inicializa sin productos. Detalle: {error}"
            )
            return []
        except PermissionError as error:
            print(f"Advertencia: no tienes permisos para leer el archivo. {error}")
            return []

        if datos is None:
            return []
        if not isinstance(datos, list):
            print("Advertencia: el contenido del archivo no es una lista válida. Se ignora.")
            return []

        productos: list[Producto] = []
        for indice, registro in enumerate(datos):
            if not isinstance(registro, dict):
                print(f"Advertencia: el registro {indice} no es un diccionario y se ignorará.")
                continue
            try:
                productos.append(Producto.from_dict(registro))
            except KeyError as error:
                print(f"Advertencia: el registro {indice} está incompleto. {error}")
            except (TypeError, ValueError) as error:
                print(f"Advertencia: el registro {indice} no es válido. {error}")
        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        try:
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
                json.dump(
                    [producto.to_dict() for producto in productos],
                    archivo,
                    ensure_ascii=False,
                    indent=2,
                )
                archivo.write("\n")
        except PermissionError as error:
            raise PermissionError(
                f"No se tienen permisos suficientes para escribir en {self.ruta_archivo}."
            ) from error
        except OSError as error:
            raise OSError(f"No se pudo guardar la información en {self.ruta_archivo}: {error}") from error
