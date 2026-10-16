"""Exercise optional installation in an isolated directory only."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def run_installer(self,path,*flags):
        return subprocess.run([sys.executable,str(ROOT/'scripts/install_codex_skill.py'),
                               '--skills-dir',str(path),*flags],capture_output=True,text=True)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'skills'
            result=self.run_installer(target,'--dry-run')
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertFalse(target.exists())

    def test_install_points_to_this_hub(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'skills'
            result=self.run_installer(target)
            self.assertEqual(result.returncode,0,result.stderr)
            files=list((target/'architecture-hub').iterdir())
            self.assertEqual({f.name for f in files},{'SKILL.md','hub-location.json'})
            config=json.loads((target/'architecture-hub/hub-location.json').read_text())
            self.assertEqual(Path(config['root']),ROOT)
            self.assertTrue((Path(config['root'])/'catalog.json').is_file())

    def test_existing_install_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(self.run_installer(folder).returncode,0)
            skill=Path(folder)/'architecture-hub/SKILL.md'
            skill.write_text('user custom content')
            self.assertEqual(self.run_installer(folder).returncode,1)
            self.assertEqual(skill.read_text(),'user custom content')

    def test_symlink_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);external=root/'external';external.mkdir();dest=root/'skills';dest.mkdir()
            (dest/'architecture-hub').symlink_to(external,target_is_directory=True)
            self.assertEqual(self.run_installer(dest).returncode,1)
            self.assertEqual(list(external.iterdir()),[])


if __name__=='__main__':unittest.main(verbosity=2)
