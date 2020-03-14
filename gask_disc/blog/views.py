from django.shortcuts import render

posts = [
    {
        'title': 'Machine Learning with TensorFlow',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum dolor sit amet, consectetur adipisicing elit. A suscipit hic odit nemo nulla, incidunt porro, in reiciendis quasi eligendi numquam laboriosam similique, explicabo accusamus quis aliquam quia, obcaecati voluptate. Natus culpa nostrum, sequi ad quam deserunt! Nemo facilis quae tempora dolore deleniti illum doloremque et, unde, quasi perferendis qui exercitationem, temporibus. Autem est maxime vero quidem natus fuga tenetur praesentium beatae saepe, magni molestias deserunt dolorem error tempore, nihil cupiditate minus assumenda. Possimus tempore asperiores officia ullam et pariatur nemo eius numquam consectetur officiis quam laudantium, ipsa rerum provident, nobis molestias minima commodi? Inventore ullam quas sed numquam magnam fugit iste praesentium dolore, atque cumque error deserunt excepturi animi veniam quam provident enim aut eligendi laudantium. Quibusdam iusto eligendi quas totam voluptas quos voluptatum sunt sint ad, doloribus temporibus voluptates reiciendis accusamus hic enim voluptate ipsam possimus, fugiat molestias consequatur, laboriosam incidunt eos. Officia dolores fugiat similique, modi ipsam. Ullam cum dolorem quibusdam!',
        'author': 'Gethsun M.',
        'date_posted': '07.03.2020'
    },
    {
        'title': 'Deploying Models',
        'content': 'Lorem ipsum dolor sit amet, consectetur Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel est, eos culpa similique dolor quam, cum, excepturi, minima quisquam quaerat et? Veritatis at molestiae, iste labore. Nam aperiam, facilis! Quasi similique, fugiat sed consequuntur accusantium illo nulla laboriosam, ullam ipsa ex aspernatur repudiandae vel. Dicta ipsa, porro enim. Reiciendis blanditiis repudiandae quo aperiam voluptatibus rem est quae facilis dolorem, officiis natus illo nemo quam excepturi repellat, illum tempora nulla impedit sed, sunt voluptas suscipit. Nulla pariatur omnis, aliquam harum debitis quasi quis modi aut, veniam quam delectus quas praesentium amet impedit nostrum ratione deserunt, iure dicta, totam alias maxime nam! adipisicing elit. Voluptas officia eum minus ad pariatur ab, quae excepturi.',
        'author': 'Gethsun M.',
        'date_posted': '07.03.2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
