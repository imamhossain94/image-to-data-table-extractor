#Image to Text Data

###Tools used
* <a href="https://pypi.org/project/Pillow/">Pillow</a>
* <a href="https://pypi.org/project/pytesseract/">PyTesseract</a>
* <a href="https://tesseract-ocr.github.io/tessdoc/Downloads">Tesseract EXE Download</a>

```
pip install Pillow
pip install pytesseract
```

###Input image
  <td width="100%"><img src="https://github.com/imamhossain94/sololearn/blob/main/table.png" alt="BLANK"></td>

###Output data
```json
{
   "header":[
      "Name",
      "Email",
      "Age",
      "Status"
   ],
   "values":[
      [
         "Leanne",
         "Graham",
         "Sincere@april.biz",
         "28",
         "Active"
      ],
      [
         "Ervin",
         "Howell",
         "Shanna@melissa.tv",
         "35",
         "Active"
      ],
      [
         "Clementine",
         "Bauch",
         "Nathan@yesenia.net",
         "33",
         "Inactive"
      ],
      [
         "Patricia",
         "Lebsack",
         "Julianne@kory.org",
         "25",
         "Active"
      ],
      [
         "Kamren",
         "Hettinger@annie.ca",
         "42",
         "Active"
      ],
      [
         "Dennis",
         "Schulist",
         "Dach@jasper.info",
         "34",
         "Inactive"
      ],
      [
         "Kurtis",
         "Weissnat",
         "Hoeger@billy.biz",
         "44",
         "Active"
      ],
      [
         "Maxime_Nienow",
         "Sherwood@rosamond.me",
         "26",
         "Active"
      ],
      [
         "Glenna",
         "Reichert",
         "McDermott@dana.io",
         "30",
         "Inactive"
      ]
   ]
}
```
