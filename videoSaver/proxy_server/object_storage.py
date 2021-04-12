#!/usr/bin/env python
#-*- coding: utf-8 -*-
import boto3

class ObjectStorage:
    def __init__(self):

        session = boto3.session.Session(
            
        )
        self.s3 = session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net'
        )

        self.bucket_name = 'test-yakovdom2'

    def create(self):
        # Создать новый бакет
        self.s3.create_bucket(Bucket=self.bucket_name)

    def save(self, key, value):
        # Загрузить объекты в бакет
        ## Из строки
        self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=value, StorageClass='COLD')
        return key
        '''
        ## Из файла
        self.s3.upload_file('this_script.py', 'bucket-name', 'py_script.py')
        self.s3.upload_file('this_script.py', 'bucket-name', 'script/py_script.py')
        '''

    def load_all(self):
        # Получить список объектов в бакете
        contents = self.s3.list_objects(Bucket=self.bucket_name)['Contents']
        for key in contents:
            print(key['Key'])
        return contents

    def delete(self):
        pass
        '''
        # Удалить несколько объектов
        forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
        response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': forDeletion})
        '''
    def load(self, key):
        # Получить объект
        get_object_response = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        #print(get_object_response['Body'].read())
        return get_object_response['Body'].read()

global_object_storage = None

def storage():
    global global_object_storage
    if global_object_storage is None:
        global_object_storage = ObjectStorage()
    return global_object_storage
