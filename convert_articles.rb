#!/usr/bin/env ruby
# Script pour convertir les articles en posts Jekyll

require 'fileutils'
require 'date'

# Créer le répertoire _posts s'il n'existe pas
FileUtils.mkdir_p("_posts") unless Dir.exist?("_posts")

# Date d'aujourd'hui pour les articles sans date
today = Date.today.strftime('%Y-%m-%d')

# Parcourir tous les fichiers markdown dans le répertoire articles
Dir.glob("articles/*.md").each do |file|
  content = File.read(file)
  filename = File.basename(file, '.md')
  
  # Extraire le titre du contenu (première ligne commençant par #)
  title_match = content.match(/^# (.+)$/m)
  title = title_match ? title_match[1].strip : filename.gsub('-', ' ').split.map(&:capitalize).join(' ')
  
  # Extraire un extrait
  content_without_title = title_match ? content.sub(/^# .+\n/, '') : content
  excerpt = content_without_title.gsub(/[#*`]/, '').strip[0..150].gsub(/\s+/, ' ') + '...'
  
  # Créer le frontmatter
  frontmatter = <<~YAML
    ---
    layout: post
    title: "#{title}"
    date: #{today} 12:00:00 +0200
    author: YayaBed
    excerpt: "#{excerpt}"
    ---
    
  YAML
  
  # Nouveau contenu avec frontmatter
  new_content = frontmatter + content
  
  # Nouveau nom de fichier au format Jekyll (_posts/YYYY-MM-DD-titre.md)
  new_filename = "_posts/#{today}-#{filename}.md"
  
  # Écrire dans le nouveau fichier
  File.write(new_filename, new_content)
  
  puts "Converti: #{file} -> #{new_filename}"
end

puts "\nConversion terminée ! Tous les articles sont maintenant dans le dossier _posts."
puts "Vous pouvez maintenant pousser ces modifications sur GitHub."
