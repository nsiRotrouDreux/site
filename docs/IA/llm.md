# Les LLM (Large langage models)

## Définition
  Un grand modèle de langage (Large Language Model, LLM) est un type de programme d'intelligence artificielle (IA) capable, entre autres tâches, de reconnaître et de générer du texte. 
  Large , en anglais grand , signifie que ce modèle est entrainé sur un nombre conséquent de données.

  Un LLM est un modèle qui a emmagasiné suffisament d'exemples pour être ensuite capable de reconnaitre une conversation et la poursuivre .

  Avant de se pencher sur le fonctionnement des LLm , un petit tour par l'hsitorique 

## Histoire des LLM

  Plutôt que de parler d'histoire, on pourrait évoquer la préhistoire des LLM dès les années 50 avec l'apparition des n-grammes : A la données d'un mot , on associe un nombre (n ici) de mots . Par exemple , au mot CHAT , on peut associer le trigramme : NOIR, SOURIS, MANGE. Ce sont des mots que le modèle va mobiliser dès qu'on lui parle de CHAT.
  On se doute que le n doit être très grand pour qu'il y ait une efficacité quelconque mais que même dans ce cas, la fluidité de la conversation n'est pas assurée. Cette approche statistiques n'est pas viable pour "une conversation cohérente".

### Les Transformers , le tournant

!!! note "Définition : Token"

     __Token__ signifie jeton en anglais .Appliqué à l'IA ce mot signifie unité de données tratitée pour l'entrainement d'une IA

  La technologie autour des transformers ( le T de transformers est le même que celui de GPT ;) apparu en 2017 a permis l'essor des LLM 

  La plus value du __Transformer__ est énorme : Au lieu de traiter les mots un par un avec les techniques précédentes , on peut désormai considérer en sa totalité, facilitant la compréhension de l'ensemble et la cohérence de la sortie proposée.

  Depuis 2017, la technologie est restée la même mais  a considérablement évolué en terme de capacités de calculs:

       * Le modèle transformer est devenue plus efficace
       * L'accès aux données est devenue encore plus massive
       * La puissance de calculs a foirtement augmenté , notamment grâce à l'esssor des GPU
!!! note " Définition : GPU"
     Un GPU est un processeur graphique dont le but premier est la création d'images et de videos.
     Mais sa forte puissance de calcul en fait un allié formidable pour les IA .
     Cette technologie a fait la fortune de la société [Nvidia](https://www.nvidia.com/fr-fr/)


  Le premier modèle de LLm accessible au grand public est le fameux Chat GPT (3). S'il est révolutionnaire , il n'empêche qu'il présente pas mal de failles dans ses réponses (voir cours sur les __biais__).

  Aujourd'hui les enjeux et les axes d'amélioration des LLM sont multiples :

   * Amélioration des réponses
   * Modèles plus spécialisés
   * Aspect énergétique
   * Alignement éthique 
   * Augmenter la part d'open source 


  

  ## Fonctionnement