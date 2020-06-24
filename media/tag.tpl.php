<?php include "html/templates/header.tpl.php" ?>

<section class="last_section catalogue">
		<div class="content-wrap">
			<div class="left-menu-wrap">
				<div class="left_menu">
					<a href="/catalog.html"><h2>каталог</h2></a>
					<ul>
						<?php mod('catalog.action.catalog'); ?>
					</ul>
					<div class="akciya">
					<a href="/akciya/145.html"><a href="/avtokosmetika_drugih_brendov.html"><img src="/img/bannerzima.jpg" alt="Новая акция"></a></a>
				</div>
				</div>
				<div class="left_menu_mobile">
					<div id="dl-menu-catalog" class="dl-menuwrapper">
						<button class="dl-trigger">Open Menu</button>
					<a href="/catalog.html"><h2>каталог</h2></a>
					<ul class="dl-menu">
						<?php mod('catalog.action.catalog_mobile'); ?>
					</ul>
					</div>
				</div>
			</div>
			<div class="main_content content">
				<?php mod( 'catalog.action.breadcrumbs' )?>
				<div class="header_border">
					<h1><?php mod( 'pages.show.title' )?></h1>
				</div>
				<?php mod( 'pages.show.content' )?>
			</div>
		</div>
	</section>


<?php include "html/templates/footer.tpl.php" ?>
