# Databricks notebook source
df = spark.range(100)
count = df.count()
print(count)
