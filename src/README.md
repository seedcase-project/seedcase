# The 100 Patients data

The 100 Patients dataset is available from
[figshare](https://doi.org/10.6084/m9.figshare.7040039.v3) as a set of
txt files. We've decided not to upload a version here, so if you would
like to load the data into your seedcase project db you will have to
download it first. The dataset contains information on diagnosis,
admissions and lab results for 100 virtual patients.

It is also possible to fetch larger dataset with 1,000 or 10,000
patients, the scripts should work with those as well.

## Download, convert, and load into Docker

This part is not yet finalised, at present it is up to the user to get
the files converted from txt to csv (please use a ; as delimiter), a
script will follow at a later date.

Download the data and convert it to csv. Make sure that the Docker
container is running before opening a terminal window. Use the cp
command to copy the csv files into the container.

``` bash
docker cp [drag and drop file name] [container name]:[destination
folder]
```

TIP: adding a /. to the folder name on your machine will get Docker to
copy all files in the folder into the container. If you only want to
copy a single file, replace the . with the full name (including
extension).

### Loading the data using a SQL management studio

Connect as normal to the database in the container and use the
`import-100patients.sql` script to fetch the data into a set of staging
tables (all data types are varchar), then run the `etl-100patients.sql`
script to move the data across to a set of table with the correct data
types.

