---
title: eBooks with Calibre e-book management, OneDrive and Android.
tags: ["apps", "ebooks", "calibre", "managment"]
---

# Introduction

[Calibre](https://calibre-ebook.com/) is an eBooks collection manager, which helps you properly organize your eBooks regardless of the format, or if you have different formats for the same title.

I use Calibre to sync and keep up-to-date my eBooks on all my devices, including my android eBooks ([ONYX BOOX Nova Pro](https://onyxboox.com/boox_novapro)). My approach:

- Calibre on Windows10/11 to manage and organize the eBooks collection
  - As possible, I always buy my eBooks DRM-free (pdf or epub), so my preferred source for books are
  - [Google Books](https://play.google.com/store/books): paid books most of them DRM-free
  - My library online branch with [OverDrive](https://www.overdrive.com/), although the app [Libby](https://www.overdrive.com/apps/libby) is great for borrowing (and works on Android eReaders)
- OneDrive (or any other cloud storage service should suffice)
  - [OneSync](https://play.google.com/store/apps/details?id=com.ttxapps.onesyncv2): to sync the files with any Android device
- eReaders: I am a big fan of [BOOX](https://www.boox.com/) Android eReaders, nothing else to say here (I personally recommend a 10.3" or 7.8", with color)

This setup is generic, so any cloud provider (or local server) with an Android/iOS sync utility should work. You can probably use the cloud provider app, but in my personal experience, the OneSync (paid version) App. has worked so well, without any issues and is so easy to configure that it was worth the cost.

# Calibre Install & Setup

* Install with default options ([link](https://calibre-ebook.com/download))
* Select _Run Calibre_ at the end of the installation

After the installation,

* Open Calibre
* The first time it will ask for the **Calibre Library** location
* Set path from Onedrive as: `OneDrive\Bibliothek\Calibre\CalibreLibrary` (or the folder structure of your preference inside OneDrive)
* E-book device: Select **Onyx** 

  > Don not select manage e-readers with Calibre, we will use the OneSync Android app.), otherwise you will need to plug the device to your computer every time you add new books
* Click on <kbd>Preferences</kbd> <kbd>Look & Feel</kbd>
  * Set `Enable system tray icon`
  * Click <kbd>Apply</kbd> <kbd>Restart calibre now</kbd>
* Click on <kbd>Preferences</kbd> <kbd>Sending books to devices</kbd>
  * set as `{#genre:subitems(0,1)}/{#genre:subitems(1,2)}/{#genre:subitems(2,3)}/{#genre:subitems(3,4)}/{#genre:subitems(4,5)}/{title} - {authors}`
  * Click <kbd>Apply</kbd> <kbd>Close</kbd>
* Click <kbd>Connect/Share</kbd> <kbd>Connect to Folder</kbd>
  * set as `OneDrive\Bibliothek\Books\Calibre`
* Verify that _On Device Column_ is set to _Main_ for all books
* **Done!**

## Plugins

* Install DeDRM Tools ([link](https://apprenticealf.wordpress.com/))
