#!/usr/bin/env ruby
# Script pour ajouter le frontmatter aux articles sans en-tête

require 'yaml'
require 'date'

# Répertoire des articles
articles_dir = 'articles'
today = Date.today.strftime('%Y-%m-%d')

# Parcourir tous les fichiers markdown dans le répertoire articles
Dir.glob("#{articles_dir}/*.md").each do |file|
  content = File.read(file)
  filename = File.basename(file, '.md')
  
  # Vérifier si le fichier a déjà un frontmatter
  if content.start_with?('---')
    puts "Le fichier #{file} a déjà un frontmatter, aucune modification nécessaire."
    next
  end
  
  # Extraire le titre du contenu (première ligne commençant par #)
  title = content.match(/^# (.+)$/m)&.[](1) || filename.gsub('-', ' ').split.map(&:capitalize).join(' ')
  
  # Créer un extrait à partir du contenu (premiers 150 caractères après le titre)
  content_without_title = content.sub(/^# .+\n/, '')
  excerpt = content_without_title.gsub(/[#*`]/, '').strip[0..150].gsub(/\s+/, ' ') + '...'
  
  # Créer le frontmatter
  frontmatter = {
    'layout' => 'article',
    'title' => title,
    'date' => "#{today} 12:00:00 +0200",
    'author' => 'YayaBed',
    'excerpt' => excerpt
  }
  
  # Ajouter le frontmatter au contenu
  new_content = "---\n#{frontmatter.to_yaml.strip}\n---\n\n#{content}"
  
  # Écrire le contenu modifié dans le fichier
  File.write(file, new_content)
  
  puts "Frontmatter ajouté à #{file}"
end

puts "\nTerminé ! Tous les fichiers sans frontmatter ont été mis à jour."
