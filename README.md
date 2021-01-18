# Thesis

 /// Instructions for English scrape (Russian and German below):
 
 Run scrape after changing the search term (see .py for more instructions).
 
 Data cleanup instructions:

 Guide for removing special characters from CSV files (remove quotation marks
 from suggested replacements and note spacing):
 
 DO THIS IN ORDER. Don't bother cleaning the title column.
 
 Replace Ã¡ with "a"
 Replace ‚¬ with " "
 Replace €¦ with " "
 Replace Ì¶ with " "
 Repkace â€“ with " "
 Replace â€˜ with startquote or " "
 Replace â€™ with endquote or " "
 Replace â€‹ with " "
 Replace â€œ with " "
 Replace â€ with " "
 Replace Ð± with " "
 Replace Â£ with " "
 Replace Â with " "
 Replace ˜ ï¸ with " "
 Replace "t.co" with " tdotco "
 Replace em (—) dash with " "
 Replace en (–) dash with " "
 Replace - with " "
 Replace apostrophes with " "
 Replace quotation marks with " "
 Replace . with " "
 Replace double spaces with single spaces (as many times as needed)
 
 If you're looking for a specific phrase with spaces (e.g. 'stop soros'),
 replace that phrase with a version without spaces (stopsoros).
 
 Be sure to clip off endings of articles that have copyright info and such.
 
 
 /// Instructions for Russian scrape (German below):
 
 Run scrape after changing the get link to the link that has both the correct
 search term and proper dates (see .py for more instructions). You will have to
 get this link by hand from russian.rt.com.
 
 Data cleanup instructions:
 
 Be sure to find and replace the following things IN THIS ORDER from the txt
 file in NotePad or equivalent:

 Russian months in genitive replaced with appropriate calendar numbers

The RT Russian disclaimer replaced with a single space (note декабря gets replaced 
with 12 and KEEP SPACES at ends of lines; this works better on Mac as in Windows
NotePad can only search for so many characters at once):
© Автономная некоммерческая организация «ТВ-Новости», 2005—2021 гг. Все права защищены. 
Сетевое изданиеrt.comзарегистрировано Роскомнадзором 21 12 2016 г., свидетельство 
Эл № ФС 77-68119 Главный редактор: Симоньян М. С. Адрес редакции: 111020, Москва, 
Боровая улица, 3к1. Телефон:+7 499 750-00-75доб. 1200 E-mail:info@rttv.ru Политика 
АНО «ТВ-Новости» в отношении обработки персональных данных Организации, признанные 
экстремистскими и запрещённые на территории РФ Данный сайт использует файлыcookies

 Guillemets « and » replaced with a single space

 Em dash — replaced with a single space

 And replace all double spaces with a single space as many times as needed.
 
 IN R: Delete tibble rows that have a skipped date. Titles are often skipped
 as they might be under a different tag.
 
 /// Instructions for German scrape:
 
 Run scrape after changing the search term (see .py for more instructions).
 
 Data cleanup instructions:
 
 Be sure to find and replace the following things IN THIS ORDER from the txt
 file in NotePad or equivalent:

 German month abbreviations replaced with appropriate calendar numbers. Some
 may have a period in them (e.g. Dez.).
 
 The RT German newsletter text replaced with a single space (may work better on
 Mac):
 Sie erhalten eine E-Mail, in der Sie Ihre Anmeldung bestätigen müssen.
 
 Replace en dash – with single space
 
 
 
 
 