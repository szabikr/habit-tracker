if [ -z ${HBT_APP_ROOT_DIR+x} ]; then
	echo "Habit Tracker App root directory (\$HBT_APP_ROOT_DIR) should be set before deploying."
	exit 1
fi

echo "deployment can start"

echo "Creating app root directory..."
mkdir $HBT_APP_ROOT_DIR
echo "Creating low level module directories..."
mkdir $HBT_APP_ROOT_DIR/activities
echo "Creating feature directories..."
mkdir $HBT_APP_ROOT_DIR/features
echo "Creating user_input directory..."
mkdir $HBT_APP_ROOT_DIR/user_input

echo "Creating data.txt file..."
touch $HBT_APP_ROOT_DIR/data.txt
echo "Creating logs.txt file..."
touch $HBT_APP_ROOT_DIR/logs.txt

cp activities/* $HBT_APP_ROOT_DIR/activities
cp features/* $HBT_APP_ROOT_DIR/features
cp log_config.yaml logging_config.py $HBT_APP_ROOT_DIR
cp main.py $HBT_APP_ROOT_DIR

cp requirements.txt $HBT_APP_ROOT_DIR
