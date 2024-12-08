<div align="center">
<img src="https://i.imgur.com/Y2XXof7.jpeg" width="900">

<br>

___

<br>

<img src="https://img.shields.io/github/license/oppsec/blobber?color=blue&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/issues/oppsec/blobber?color=blue&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/stars/oppsec/blobber?color=blue&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/forks/oppsec/blobber?color=blue&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/languages/code-size/oppsec/blobber?color=blue&logo=github&style=for-the-badge">

</div>

<br>

<h3> Blobber - Azure Blob Storage Service Enumeration Tool </h2>
<p> <b>Blobber</b> is a tool focused on enumerating files stored in an Azure Blob Storage Service with anonymous access enabled. </p>

<br>

<h3> Installation </h3>
<pre>
~$ apt install pipx
~$ pipx ensurepath
~$ pipx install git+https://github.com/oppsec/blobber.git
~$ blobber
</pre>

<br>

<h3> Usage examples </h3>
<pre>
blobber -u "https://target.com/uploads"
blobber -u "https://target.com/assets" -f '.pdf'
</pre>

<br>

<h3> Updating </h4>
<pre>
1. option: pipx install git+https://github.com/oppsec/blobber.git --force
2. option: pipx reinstall blobber --python /usr/bin/python
</pre>

<br>


<h3> Warning </h3>
<p> The developer is not responsible for any malicious use of this tool </p>
