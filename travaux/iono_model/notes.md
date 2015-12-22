## Notes générales:
- Altitude des satellites GPS: environ 20 200Km
- ionosphere entre 60 et 1500km
- Le changement de la vitesse, forme, ... du signal GPS est du aux électrons libres présents dans l'ionosphere
- L'inosphere change avec le temps et l'espace (cuncpot cycle, seasonal and diurnal... régions sur le globe terrestre)
- Faire attention dans les zones equatoriales (10° et 15° nord et sud ) à cause de l'anomalie d'Appleton(Doherty et al. 2002).
- Le paramètre qu'il faut modéliser dans l'IONO est le TEC pour pouvoir corriger le signal GPS, Le retard ionospherique d'une onde radio est proportionnel au TEC
- TEC est l'intégrale de la densité des électrons sur 1 m2 au long du trajet de l'onde
- 10^16 electrons/m2 = 1 TECU (Abdullah, 2009)
- le TEC varie entre 10^16 et 10^19 avec le min et le max enregitrés à midi et minuit.
- L'iono est constitué de régions chaque région est constitué de couches. La région F(appleton-Barnett layer) qui s'étale de 150-800 Km d'altitude. Cette région nous intéresse plus particulièrement parce qu'elle est connue pour la grande variabilité de ses électrons
- Pour modéliser le retard iono il faut calculer TSCv (vertical ne dépent pas de la localisation du satellite) et TECs (slant dépent de la localisation du satellite)
- pour Obtenir TECs tout long de LOS (Line Of Sight) on utilise et les mesures de phase et les mesures de pseudo-distance.
- On considère 



## A voir:
- carrier phase smoothing technique. (bien explique dans papier université calgary) 

## constantes:
- L1 = 1575.42Mhz et L2 = 1227.60Mhz
