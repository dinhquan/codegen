//
//  __FileName__
//  __ProjectName__
//
//  Created by __UserName__ on __Date__.
//  Copyright (c) __Year__ __OrganizationName__. All rights reserved.
//


import UIKit

final class __ModuleName__Wireframe: BaseWireframe {

    // MARK: - Private properties -

    // MARK: - Module setup -

    init() {
        let moduleViewController = __ModuleName__ViewController()
        super.init(viewController: moduleViewController)

        let interactor = __ModuleName__Interactor()
        let presenter = __ModuleName__Presenter(view: moduleViewController, interactor: interactor, wireframe: self)
        moduleViewController.presenter = presenter
    }

}

// MARK: - Extensions -

extension __ModuleName__Wireframe: __ModuleName__WireframeInterface {
}
