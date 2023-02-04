import requests
from bs4 import BeautifulSoup

# College link examples frm the sheet.

All_url = ['http://www.useams.org/',
    'https://www.amclko.org/',
    'http://ascomscollege.com/',
    'https://www.acharya.ac.in/',
    'https://pgcollegekawardha.edu.in/',
    'http://acmecollege.com/',
    'http://www.adarshcollegeedu.co.in/ContactUs.aspx',
    'http://www.adhiyamaanpolytech.in/',
    'https://www.aec.edu.in/',
    'http://www.adityatekkali.edu.in/',
    'https://www.asci.org.in/',
    'http://www.agmc.nic.in/',
   'https://atc.edu.in/',
    'https://ammcollege.in/',
    'https://alipurduarcollege.ac.in/',
    'https://www.aiimsjodhpur.edu.in/',
    'https://aiimsbhopal.edu.in/index_controller/index',
   'http://www.aceatech.com/',
    'http://actripura.edu.in/',
   'https://aimsbschool.org/',
    'https://www.amity.edu/jaipur/abs/',
    'http://amjadalikhancollege.edu.in/',
    'http://ampatidegreecollege.in/',
    'https://www.accommercejpg.org/',
    'https://www.actrainingcollege.org/',
    'http://www.actc.edu.in/',
    'http://www.andhraloyolacollege.ac.in/',
    'http://www.amc.edu.in/',
    'https://anits.edu.in',
    'http://anushreecollege.com/home.php',
    'http://apscollegeofnursing.com/',
    'http://www.aqjpgstudies.org/',
    'http://www.arghpharmacy.ac.in/',
    'http://www.arafatrust.org/arafa_arts_science.html',
    'https://aimri.in/',
    'http://www.samcpatna.org/',
    'http://www.apied.edu.in/',
    'https://www.aryamgt.ac.in/',
    'http://aryanedu.com/',
    'http://www.aryavartgyan.com/'
    'http://ashaacademy.org/',
    'https://www.asadi.edu.in/',
    'http://sriasnmgdcpalakol.in/',
    'http://asrgroup.co.in/asrcoe/',
    'http://avanthienggcollege.ac.in/',
    'http://avinuty.ac.in/maincampus/',
    'http://bssmc.in/',
    'https://bfitdoon.com/',
    'https://hte.rajasthan.gov.in/college/gcaalwar',
    'http://www.bkmp.cteguj.in/',
    'https://www.bakshirhatmahavidyalaya.org/',
    'http://www.bcop.net/',
    'http://www.becbapatla.ac.in/',
    'https://www.bvvsbscbgk.org/',
    'http://bimt.org.in/',
    'https://bgcl.net.in/',
    'https://bgiet.ac.in/',
    'https://bgin.co.in/',
    'https://bgpc.in/',
    'http://www.bskmcollege.info/',
    'https://govtbpdpgcollege.com/',
    'https://www.bharathuniv.ac.in/',
    'http://www.btcstagartala.org/',
    'https://bit.edu.in/',
    'https://biharcollegeofpharmacy.com/',
    'http://www.bijanbaridegreecollege.org/']

for url in All_url:
    r = requests.get(url)
    Html_content = r.content
    soup = BeautifulSoup(Html_content, 'html.parser')
    t = soup.title
    print(f"college name-{t.string }\n\n\n")
    anchors = soup.find_all('a')
    for link in anchors:
        if (link.get('href')!='#'):
            if "contact-us/" in link.get('href'):
                link_text = url + link.get('href')
                link_data = soup.find('div').get_text()
                print(link_data)
