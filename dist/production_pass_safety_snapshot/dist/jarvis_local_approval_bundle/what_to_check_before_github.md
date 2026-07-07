# What To Check Before GitHub

Before uploading or pushing:

1. Run the local preview.
2. Confirm the phone frame looks like the final app, not a development harness.
3. Confirm there is no Recent Activity, large response panel, guide text, data dump, or debug chip in the phone frame.
4. Confirm the top-right help icon opens concise help.
5. Confirm the top-left Mesh control is understandable.
6. Confirm keyboard compact mode does not clip required elements.
7. Confirm scan, read, and detect are the primary review commands.
8. Confirm Control Mesh commands give exact next actions.
9. Run the full local tests with `run_tests.bat`.
10. Read `latest_test_report.txt`.
11. Review `screens_to_review.md`.
12. Only after visual approval, use GitHub Actions to compile the Swift app.
