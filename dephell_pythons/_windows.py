# built-in
from pathlib import Path
from typing import List

# external
from packaging.version import Version

# app
from ._cached_property import cached_property
from ._python import Python


class WindowsFinder:
    @cached_property
    def pythons(self) -> List[Python]:
        from .pep514tools import findall

        pythons = []
        for env in findall():
            d = env.info._d
            path = getattr(d.get('InstallPath'), 'executable_path', None)
            if path is None:
                path = getattr(d.get('InstallPath'), '', None)
                if path is None:
                    continue
            version = str(d['Version'])
            # conda returns it's own version
            if version[0] not in '23':
                continue
            python = Python(
                path=path,
                version=Version(version),
                implementation='python',  # TODO: guess architecture
            )
            python.lib_paths = self._get_lib_paths(env)
            pythons.append(python)
        return pythons

    @staticmethod
    def _get_lib_paths(env) -> List[Path]:
        paths = []
        libs = env.info._d['PythonPath']._d[''].split(';')
        for path in libs:
            path = Path(path)
            if 'Scripts' not in path.parts:
                paths.append(path)
        return paths
