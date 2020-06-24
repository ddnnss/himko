<?php
	$table_page = new Table( "pages" );
	$pages = $table_page->select( "SELECT * FROM `pages` WHERE `alias`=:alias LIMIT 1", array('alias' => $alias) );
$test = $table_page->select( "SELECT alias FROM `pages` WHERE `tag`=:tag", array('tag' => $alias) );
print_r($alias);

echo $alias;
		

?>
