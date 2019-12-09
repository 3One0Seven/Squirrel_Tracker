from django.http import HttpResponse
from django.shortcuts import render

def home(*args, **kargs):
	return HttpResponse(
		'''<!DOCTYPE html>
				<html>
				<head>
					<title>Squirrel Tracker</title>
					<center><h1 style="font-size: 100px">Squirrel Tracker</h1></center>
				</head>
				<body>
					<style>
				      ul {
				      list-style-type: none;
				      margin: 0;
				      padding: 0;
				      overflow: hidden;
				    }

				    li {
				      float: center;
				    }

				    li a {
				      font-size: 50px;
				      font-weight: bold;
				      display: block;
				      color: black;
				      text-align: center;
				      padding: 50px 60px;
				      text-decoration: none;
				    }

				    li a:hover {
				      background-color: #dddddd;
				    }
				    </style>
				  <ul>
				  <li><a href="/map">Map</a></li>
				  <li><a href="/sightings">Squirrels List</a></li>
				  </ul>
				</body>
				</html>
				''')