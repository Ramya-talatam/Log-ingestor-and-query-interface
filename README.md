<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2sZOX9xt)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Log Ingestor and Query Interface</h3>

  <p align="center">
    This project provides a simple log ingestion system and querying interface built with Flask, html and MongoDB Atlas. It allows users to ingest logs over HTTP and query logs based on various criteria.
    <br />
    <a href="https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam/issues">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#system-design">System Design</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Log Ingestion:
* The client sends a POST request to /ingest_logs with a JSON payload containing logs.
* The Flask server processes the request, extracts log data, and inserts it into the MongoDB collection.
  
Log Querying:
* The client interacts with the HTML interface, specifying criteria for log querying.
* The HTML interface sends a GET request to /query_logs with query parameters.
* The Flask server processes the query parameters, retrieves matching logs from the MongoDB collection, and returns the results to the client.
* 
### System Design
![system_design_diagram](https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam/assets/108510824/601b0a80-1921-41ff-91c1-113310196ff1)
Flask Web Server:
* Log Ingestion Endpoint: Exposes an endpoint (/ingest_logs) to receive logs via HTTP POST requests.
* Querying Interface Endpoint: Provides an endpoint (/query_logs) to query logs based on specified criteria.
* HTML Interface: Serves an HTML page for users to interact with the querying interface.

MongoDB Database:
* Log Collection: Stores logs in a MongoDB collection. Each log entry is a document with fields such as "level," "message," "timestamp," etc.

Client (e.g., Web Browser):
* Interacts with the HTML Interface: Users can input query parameters and submit requests to the Flask server for log querying.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python
* Flask
* MongoDB Atlas
* html

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
Follow the below instructions to set up and run the project locally.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python3
* Flask==2.0.1
* pymongo==3.12.1
  
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam.git
   ```
2. Install FLask
   ```sh
   pip install Flask

   ```
3. Install PyMongo
   ```sh
   pip install pymongo

   ```

### steps to run
* open source-code folder and follow below steps.
* for log ingestion, in CLI type below commands and hit enter.
   ```sh
   python log_ingestor.py
   ```
* Run the below script in powershell to populate logs while log_ingestor.py is still running: 
   ```sh  
    $logs = Get-Content -Raw -Path .\logs.json | ConvertFrom-Json
    $url = "http://localhost:3000/ingest"
    $headers = @{
        "Content-Type" = "application/json"
    }
    foreach ($log in $logs) {
        $logJson = $log | ConvertTo-Json
        Invoke-WebRequest -Uri $url -Method Post -Headers $headers -Body $logJson
    }
   ```
* for querying logs,
    ```sh
   python query_interface.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ROADMAP -->
## Roadmap

- [x] Develop a mechanism to ingest logs in the provided format.
- [x] Offer a user interface (Web UI) for full-text search across logs including filters.
- [x] Aim for efficient and quick search results.
- [x] Advanced Features (Bonus):
    - [x] Utilize regular expressions for search.
    - [x] Allow combining multiple filters.
    - [x] cloud-based solutions can ensure robust scalability
    - [ ] implementing hybrid database solutions (relational + NoSQL).

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Ramya Talatam - (https://www.linkedin.com/in/ramya-talatam)

Project Link: [github-repo](https://github.com/dyte-submissions/november-2023-hiring-Ramya-talatam)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]:  https://www.linkedin.com/in/ramya-talatam
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 