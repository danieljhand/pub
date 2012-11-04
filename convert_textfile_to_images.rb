#! /usr/bin/ruby -w
require 'rubygems'
require 'RMagick'

# Take input text file name as input
text_file = ARGV[0]

# Take output directory as input
output_dir = ARGV[1]

# Open input text file and loop through each line
File.open(text_file, "r").each_line do |line|

  canvas = Magick::ImageList.new
  canvas.new_image(1200, 200)

  text = Magick::Draw.new
  text.font_family = 'helvetica'
  text.pointsize = 36
  text.font_weight = 700
  text.gravity = Magick::CenterGravity

  text.annotate(canvas, 0,0,2,2, line) {
    self.fill = 'black'
  }

  canvas.write(output_dir + line + '.gif')
end

exit
