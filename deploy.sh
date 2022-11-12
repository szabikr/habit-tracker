if [ -z ${HBT_APP_ROOT_DIR+x} ]; then
	echo "Habit Tracker App root directory (\$HBT_APP_ROOT_DIR) should be set before deploying."
	exit 1
fi

echo "Create app root directory..."
mkdir $HBT_APP_ROOT_DIR

echo "Create package directories..."
mkdir $HBT_APP_ROOT_DIR/ht_models
mkdir $HBT_APP_ROOT_DIR/ht_parser
mkdir $HBT_APP_ROOT_DIR/ht_builder
mkdir $HBT_APP_ROOT_DIR/ht_importer

echo "Create user_input directory..."
mkdir $HBT_APP_ROOT_DIR/user_input

echo "Create database files..."
touch $HBT_APP_ROOT_DIR/activity.txt
touch $HBT_APP_ROOT_DIR/journal_entry.txt

echo "Create cache files..."
touch $HBT_APP_ROOT_DIR/cache.txt

echo "Copy packages..."
cp ht_models/* $HBT_APP_ROOT_DIR/ht_models
cp ht_parser/* $HBT_APP_ROOT_DIR/ht_parser
cp ht_builder/* $HBT_APP_ROOT_DIR/ht_builder
cp ht_importer/* $HBT_APP_ROOT_DIR/ht_importer

echo "Copy setup files..."
cp setup.py setup.cfg $HBT_APP_ROOT_DIR

echo "Copy main script..."
cp main.py $HBT_APP_ROOT_DIR

echo "Copy README.md file..."
cp README.md $HBT_APP_ROOT_DIR
