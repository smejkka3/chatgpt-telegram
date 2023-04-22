#!/usr/bin/python
import psycopg2

from pathlib import Path
from loguru import logger

from configparser import ConfigParser
import yaml
from yaml.loader import SafeLoader

def config(path, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(path)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, path))

    return db

def connect(configuration):
    """ Connect to the PostgreSQL database server """
    conn = None
    resources_paths = configuration.get('run_resources').get('paths')
    populate_db_template = Path(resources_paths.get('populate_db_test')).open().read()
    create_db_template = Path(resources_paths.get('init_db')).open().read()
    secrets_paths = resources_paths.get('db_params')
    #try:
    # read connection parameters
    params = config(secrets_paths)

    # connect to the PostgreSQL server
    logger.info('Connecting to the PostgreSQL database...')
    logger.info(params)
    conn = psycopg2.connect(**params)
    
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # execute a statement
    logger.info('PostgreSQL database version:')
    cursor.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cursor.fetchone()
    logger.info(db_version)

    #Retrieving data
    cursor.execute(f'''{create_db_template}''')

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()
        
	# close the communication with the PostgreSQL
    #     cur.close()
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')

if __name__ == "__main__":
    configurations = yaml.load(open('assets/configurations/run_configs.yml'), Loader=SafeLoader)

    connect(configurations)