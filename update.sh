python3 get-building-names.py
echo "Retrieved building names"
python3 covid_buildings.py
echo "Updated building statuses"
python3 kml_parse.py
echo "Updated webpage"
git add .
git commit -m "auto"
git push origin master
echo "Update complete"
