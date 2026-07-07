@echo off
cd /d "%~dp0\..\.."
python tools\prepare_visual_assets.py
python core\registry\validate_registry.py
python native\ios\JarvisShell\scripts\generate_models.py
python tests\run_all_tests.py
python preview\windows_jarvis_preview\jarvis_preview.py --self-test
python tools\jarvis_interaction_test.py
